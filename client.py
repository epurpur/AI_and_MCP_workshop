import asyncio
import json
import ollama
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# server runs in the background and is called asynchronously
async def main():   
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"]       #MCP server file is referenced here
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # Discover available resources
            tools = await session.list_tools()
            print("Available tools:", [t.name for t in tools.tools])


            # Discover available resources
            resources = await session.list_resources()
            print()
            print("Available resources:", [r.uri for r in resources.resources])

            for r in resources.resources:
                print(json.dumps({
                    "uri": str(r.uri),
                    "name": r.name,
                    "description": r.description,
                    "mime_type": r.mime_type
                }, indent=2))

            # Read a resource's content
            resource_result = await session.read_resource("cities://supported")
            for content in resource_result.contents:
                print("Resource content:", content.text)

            # Discover available prompts
            prompts = await session.list_prompts()
            print()
            print("Available prompts:", [p.name for p in prompts.prompts])

            for p in prompts.prompts:
                print(json.dumps({
                    "name": p.name,
                    "description": p.description,
                    "arguments": [a.name for a in (p.arguments or [])]
                }, indent=2))    

            # This line must exist before "question" is used anywhere below
            question = "What should I see in San Francisco?"  
            print(f"Question: {question}")

            response = ollama.chat(
                model="llama3.2:latest",
                messages=[{"role": "user", "content": question}],
                tools=[{
                    "type": "function",
                    "function": {
                        "name": t.name,
                        "description": t.description,
                        "parameters": t.input_schema
                    }
                } for t in tools.tools]
            )

            if response.message.tool_calls:
                tool_call = response.message.tool_calls[0]
                result = await session.call_tool(
                    tool_call.function.name,
                    arguments=tool_call.function.arguments
                )
                tool_result_text = result.content[0].text
                print(tool_result_text)

            else:
                print(f"Answer: {response.message.content}")

asyncio.run(main())