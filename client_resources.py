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

            # Read all available resources dynamically
            for r in resources.resources:
                result = await session.read_resource(r.uri)
                for content in result.contents:
                    print(f"{r.uri} ->", content.text)

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



asyncio.run(main())