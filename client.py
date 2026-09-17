# client.py
import asyncio
import json
import ollama
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"]
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools = await session.list_tools()
            print("Available tools:", [t.name for t in tools.tools])

            # This line must exist before "question" is used anywhere below
            question = "What's there to do in New York?"  ##### START HERE. HOW DO I GET IT TO GO BETWEEN TOOLS?
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

                # final_response = ollama.chat(
                #     model="llama3.2:latest",
                #     messages=[
                #         {"role": "user", "content": question},
                #         response.message,
                #         {"role": "tool", "content": tool_result_text}
                #     ]
                # )
                # print(f"Answer: {final_response.message.content}")
            else:
                print(f"Answer: {response.message.content}")

asyncio.run(main())