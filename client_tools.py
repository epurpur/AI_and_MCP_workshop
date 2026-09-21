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


            # This line must exist before "question" is used anywhere below
            question = "\n What is the weather like in San Francisco?"  
            print(f"Question: {question}")

            # # Example 2
            # question = "\n What is there to do for fun in New York?"  
            # print(f"Question: {question}")

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

                # Print which tool was chosen and with what arguments
                print(f"\n LLM chose tool: {tool_call.function.name}")
                print(f"With arguments: {tool_call.function.arguments}")

                result = await session.call_tool(
                    tool_call.function.name,
                    arguments=tool_call.function.arguments
                )
                tool_result_text = result.content[0].text
                print()
                print(tool_result_text)

            else:
                print(f"\n Answer: {response.message.content}")

asyncio.run(main())