""" MCP server for Gallagher access control systems
"""

from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="gallagher")


# Add your tools here, for example:
@mcp.tool()
def list_divisions():
    """List all divisions in the Command Centre"""
    # Implementation here
    return ["Division A", "Division B", "Division C"]

@mcp.tool()
def add_user(username: str, division_id: int):
    """Add a new user to a division in the Command Centre"""
    # Implementation here
    pass


@mcp.tool()
def list_all_users():
    """List all users in the Command Centre"""
    # Implementation here
    return ["User1", "User2", "User3"]