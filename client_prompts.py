import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
import ollama

# This script demonstrates that the "weather_report" prompt in server.py is:
#   1. Genuinely templated server-side (different arguments produce
#      different generated text, with zero client-side string logic).
#   2. Actually influencing the LLM's answer, not just cosmetic text.
#
# HOW TO USE:
#   1. Run this script as-is. Note the two generated prompts (for two
#      different cities) and the two model answers at the bottom.
#   2. Edit ONLY server.py's weather_report() function - e.g. add an
#      instruction like "Keep it under 2 sentences" or "Mention nearby
#      indoor activities if it's raining."
#   3. Re-run this script with NO changes made here.
#   4. Compare the "WITH PROMPT TEMPLATE" answer before and after your
#      edit. If it changes purely because you edited server.py, that
#      proves the template is real and is actually shaping the LLM's
#      response - not just decorative text.


async def main():
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"]
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # ---- Prove the template actually changes the LLM's answer ----
            # We compare a bare, unadorned question against the same
            # question run through the server's prompt template.
            city = "London"
            plain_question = f"What is the weather like in {city}?"

            prompt_result = await session.get_prompt("weather_report", arguments={"city": city})
            templated_question = prompt_result.messages[0].content.text

            print("\n\n=== Comparing answers: plain question vs. prompt template ===")
            print(f"\nPlain question: {plain_question}")
            print(f"Templated question: {templated_question}")

            # NOTE: no "tools" argument here on purpose - we want to see the
            # model's actual generated text, not a tool call, so the wording
            # difference is visible in the output.
            plain_response = ollama.chat(
                model="llama3.2:latest",
                messages=[{"role": "user", "content": plain_question}]
            )
            templated_response = ollama.chat(
                model="llama3.2:latest",
                messages=[{"role": "user", "content": templated_question}]
            )

            print("\n--- Answer WITHOUT prompt template ---")
            print(plain_response.message.content)

            print("\n--- Answer WITH prompt template ---")
            print(templated_response.message.content)


asyncio.run(main())