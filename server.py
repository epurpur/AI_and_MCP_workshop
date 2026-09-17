# server.py — back to the clean version, no debug block needed here
from mcp.server.mcpserver import MCPServer

mcp = MCPServer("weather-demo")

@mcp.tool()
def get_weather(city: str) -> str:
    """Get the current weather for a given city."""
    fake_weather_data = {
        "san francisco": "62°F, foggy",
        "new york": "71°F, sunny",
        "london": "58°F, rainy",
    }
    return fake_weather_data.get(city.lower(), "No data for that city")

def get_attractions(city: str) -> str:
    """Get the list of attractions in a given city."""
    fake_attractions_data = {
        "san francisco": "Golden Gate Bridge",
        "new york": "times square",
        "london": "buckingham palace"
    }

@mcp.resource("cities://supported")
def supported_cities() -> str:
    """List of cities this server has data for."""
    return "San Francisco, New York, London"

if __name__ == "__main__":
    mcp.run()