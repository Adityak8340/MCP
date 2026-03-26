import random
from fastmcp import FastMCP

#Create  a FastMCP server
mcp = FastMCP(name="My FastMCP Server")

@mcp.tool
def roll_dice(n_dice: int = 1) -> list[int]:
    """Roll a specified number of dice and return the results."""
    return [random.randint(1, 6) for _ in range(n_dice)]

@mcp.tool
def add_numbers(a: float, b: float) -> float:
    """Add two numbers and return the result."""
    return a + b

if __name__ == "__main__":
    mcp.run()

# uv run fastmcp dev inspector main.py:mcp