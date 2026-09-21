
from mcp.server.mcpserver import MCPServer

#this actually instantiates the server. Think of it like an empty filing cabinet to which you give a label
mcp = MCPServer("demo-server")

##TOOLS
#must declare each function as an MCP tool in order to call it from LLM
@mcp.tool()  #python decorator. This basically just extends the functionality of this function to the end of the code block 
def get_weather(city: str) -> str:
    """Get the current weather for a given city."""  #docstring is what is actually read by the LLM
    fake_weather_data = {
        "san francisco": "62°F, foggy",
        "new york": "71°F, sunny",
        "london": "58°F, rainy",
    }
    return fake_weather_data.get(city.lower(), "No data for that city")

@mcp.tool()
def get_attractions(attraction: str) -> str:
    """Get the list of attractions in a given city."""
    fake_attractions_data = {
        "san francisco": "Golden Gate Bridge",
        "new york": "times square",
        "london": "buckingham palace"
    }
    return fake_attractions_data.get(attraction.lower(), "No data for that city")

##RESOURCES
#must declare each resource as an MCP resource in order for LLM to read it
@mcp.resource("cities://supported")     
def supported_cities() -> str:
    """List of cities this server has data for. These are international cities that people want information about."""
    return "San Francisco, New York, London"

@mcp.resource("attractions://supported")
def supported_attractions() -> str:
    """List of attractions this server has data for. These are well known attractions that people want to visit."""
    return "Golden Gate Bridge, Times Square, Buckingham Palace"


##PROMPTS
#must declare each prompt as an MCP prompt in order for LLM to use
@mcp.prompt()
def weather_report(city: str) -> str:
    """Generate a friendly weather report prompt for a given city."""
    return f"Please give me a detailed, friendly weather report for {city}, including whether I should bring an umbrella or jacket."



if __name__ == "__main__": #this just checks if a python file is being run directly of it if is being imported as another module/file
    mcp.run()