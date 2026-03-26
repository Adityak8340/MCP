# FastMCP Demo Server

A demo project for learning the **Model Context Protocol (MCP)** using [FastMCP](https://github.com/jlowin/fastmcp) — a fast, Pythonic way to build MCP servers.

## Prerequisites

- **Python 3.13+**
- **[uv](https://docs.astral.sh/uv/)** — a fast Python package manager

## Setup

### 1. Install uv

```bash
# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Create and initialize the project

```bash
mkdir fastmcp-demo-server
cd fastmcp-demo-server
uv init
```

### 3. Add FastMCP dependency

```bash
uv add fastmcp
```

### 4. Verify FastMCP version

```bash
uv run fastmcp version
```

## Server Code

The server is defined in `main.py` and exposes two tools:

| Tool | Description |
|------|-------------|
| `roll_dice(n_dice)` | Roll one or more dice and return the results |
| `add_numbers(a, b)` | Add two numbers and return the result |

```python
import random
from fastmcp import FastMCP

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
```

## Running the Server

### Dev mode (with MCP Inspector)

Launch an interactive inspector UI to test your tools in the browser:

```bash
uv run fastmcp dev main.py
```

### Production mode

Run the server directly via stdio transport:

```bash
uv run fastmcp run main.py
```

### Install to Claude Desktop

Register this server with the Claude Desktop app so Claude can call your tools:

```bash
uv run fastmcp install main.py
```

This adds the server to Claude Desktop's MCP configuration. Once installed, Claude can invoke `roll_dice` and `add_numbers` directly during conversations.

## Project Structure

```
fastmcp-demo-server/
├── main.py          # MCP server with tool definitions
├── pyproject.toml   # Project metadata and dependencies
└── README.md
```

## Resources

- [Model Context Protocol Specification](https://modelcontextprotocol.io/)
- [FastMCP Documentation](https://gofastmcp.com)
- [uv Documentation](https://docs.astral.sh/uv/)
