from mcp.server.fastmcp import FastMCP

mcp = FastMCP('Demo')

@mcp.tool()
def add(a:int,b:int)->int :
    """ add two numbers"""
    return a+b