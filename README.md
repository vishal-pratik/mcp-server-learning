# MCP Server - Learning Project

A Model Context Protocol (MCP) server that provides basic arithmetic tools for Claude Desktop and other MCP clients.

## Features

This MCP server currently provides:
- **add** - A tool to add two integers and return the sum

## Installation

### Using with Claude Desktop

Add this configuration to your Claude Desktop config file:

**macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "add_tool": {
      "command": "uvx",
      "args": [
        "--native-tls",
        "--from",
        "git+https://github.com/vishal-pratik/mcp-server-learning.git",
        "mcp-server"
      ]
    }
  }
}
```

**Note:** Adjust the `command` path to point to your `uvx` installation location. You can find it with:
```bash
which uvx
```

### Local Development

1. Clone the repository:
```bash
git clone https://github.com/vishal-pratik/mcp-server-learning.git
cd mcp-server-learning
```

2. Install dependencies:
```bash
uv sync
```

3. Run the server:
```bash
uv run --native-tls mcp-server
```

## Usage

Once configured in Claude Desktop, you can use the tools by asking Claude:

> "Can you add 25 and 17 for me?"

Claude will automatically use the `add` tool from this MCP server to perform the calculation.

## Project Structure

```
.
├── src/
│   └── mcpserver/
│       ├── __init__.py
│       ├── __main__.py      # Entry point
│       └── deployment.py    # FastMCP server with tools
├── pyproject.toml          # Project configuration
├── uv.lock                # Dependency lock file
└── README.md
```

## Tools

### add(a: int, b: int) -> int

Adds two integers and returns their sum.

**Parameters:**
- `a` (int): First number
- `b` (int): Second number

**Returns:** Sum of a and b

**Example:**
```python
add(5, 3)  # Returns 8
```

## Requirements

- Python >= 3.13
- mcp[cli] >= 1.26.0

## Development

To add more tools to this server, edit `src/mcpserver/deployment.py`:

```python
@mcp.tool()
def your_new_tool(param: str) -> str:
    """Description of what your tool does"""
    return f"Result: {param}"
```

## Troubleshooting

### Certificate Issues

If you encounter TLS certificate errors, ensure you're using the `--native-tls` flag:

```bash
uvx --native-tls --from git+https://github.com/vishal-pratik/mcp-server-learning.git mcp-server
```

### Server Not Starting

1. Check that uvx is installed: `which uvx`
2. Verify Python version: `python --version` (should be 3.13+)
3. Check Claude Desktop logs for error messages

## License

MIT

## Author

Vishal Pratik
