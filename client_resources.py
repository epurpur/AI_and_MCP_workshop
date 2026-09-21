import asyncio
import json
import ollama
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# This script picks WHICH resource to fetch dynamically, based on the
# user's question, instead of hardcoding a URI like "cities://supported".
#
# How the selection works:
#   1. We list all resources the server exposes (name + description).
#   2. We ask the LLM itself to pick the single most relevant resource
#      (or "none") for the current question, the same way it picks tools.
#   3. Only that resource gets fetched via MCP and injected into context.
#   4. The main chat call then runs with that context, and may call a tool.


async def choose_resource(question: str, resources) -> str | None:
    """Ask the LLM which resource (if any) is relevant to the question.
    Returns a resource URI string, or None if no resource applies."""

    resource_list = "\n".join(
        f"- {r.uri} : {r.description}" for r in resources
    )

    selection_prompt = (
        "You are selecting which reference resource (if any) is relevant "
        "to a user's question. Respond with ONLY the resource URI that is "
        "most relevant, or the word NONE if none apply. Do not explain.\n\n"
        f"Available resources:\n{resource_list}\n\n"
        f"Question: {question}"
    )

    response = ollama.chat(
        model="llama3.2:latest",
        messages=[{"role": "user", "content": selection_prompt}]
    )

    choice = response.message.content.strip()

    valid_uris = {str(r.uri) for r in resources}
    if choice in valid_uris:
        return choice
    return None


async def main():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"]
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools = await session.list_tools()
            tool_schema = [{
                "type": "function",
                "function": {
                    "name": t.name,
                    "description": t.description,
                    "parameters": t.input_schema
                }
            } for t in tools.tools]

            resources = (await session.list_resources()).resources
            print("Available resources:")
            for r in resources:
                print(f"  {r.uri} : {r.description}")

            # This line must exist before "question" is used anywhere below
            question = "What is the weather like in London?"
            print(f"\nQuestion: {question}")

            # # This line must exist before "question" is used anywhere below
            # question = "What is there to do in New York?"
            # print(f"\nQuestion: {question}")

            chosen_uri = await choose_resource(question, resources)

            if chosen_uri:
                print(f"-> LLM selected resource: {chosen_uri}")
                result = await session.read_resource(chosen_uri)
                resource_text = result.contents[0].text
                print(f"   Resource content: {resource_text}")
                system_content = (
                    f"Relevant reference data ({chosen_uri}): {resource_text}"
                )
            else:
                print("-> LLM selected no resource")
                system_content = "No additional reference data is relevant."

            response = ollama.chat(
                model="llama3.2:latest",
                messages=[
                    {"role": "system", "content": system_content},
                    {"role": "user", "content": question}
                ],
                tools=tool_schema
            )

            if response.message.tool_calls:
                tool_call = response.message.tool_calls[0]
                print(f"Tool called: {tool_call.function.name}({tool_call.function.arguments})")
                result = await session.call_tool(
                    tool_call.function.name,
                    arguments=tool_call.function.arguments
                )
                print("Tool result:", result.content[0].text)
            else:
                print("Model answered directly:", response.message.content)


asyncio.run(main())