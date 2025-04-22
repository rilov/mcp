from mcp.server.fastmcp import FastMCP 

mcp =FastMCP("Weather") 


@mcp.tool()
def forcast(city: str) -> int:
    return "Response from weather forecast service.. Nice weather today"


if __name__ =="__main__":
    mcp.run(transport="stdio")