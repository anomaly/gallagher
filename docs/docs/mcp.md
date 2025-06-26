# MCP (Model Context Protocol) Server

The Gallagher Command Centre toolkit includes an MCP server that exposes cardholder querying functionality through the Model Context Protocol. This allows AI assistants to query Gallagher Command Centre data directly.

## Overview

The MCP server provides tools for:

- Listing all cardholders in the system
- Searching for cardholders by name or other criteria
- Getting detailed information about specific cardholders
- Retrieving cards assigned to cardholders
- Getting access groups assigned to cardholders

## Installation

The MCP dependencies are included in the main package. No additional installation is required.

## Configuration

### Environment Variables

The MCP server requires the following environment variable:

- `GACC_API_KEY`: Your Gallagher Command Centre API key

### Setting up the API Key

```bash
export GACC_API_KEY="your-gallagher-api-key-here"
```

## Usage

### Running the MCP Server

#### Via CLI

```bash
# Start the MCP server (stdio mode)
gala mcp serve

# Start the MCP server (TCP mode)
gala mcp serve --port 8080 --host 0.0.0.0

# Show configuration information
gala mcp config

# Test the server functionality
gala mcp test
```

#### Direct Module Execution

```bash
# Stdio mode (default)
python -m gallagher.mcp

# TCP mode
python -m gallagher.mcp.server --port 8080 --host 0.0.0.0
```

### Transport Modes

The MCP server supports two transport modes:

#### Stdio Mode (Default)

- Runs on standard input/output
- Used by MCP clients that spawn subprocesses
- Secure for local use
- No network exposure

#### TCP Mode

- Runs on a network port
- Accessible via HTTP
- Suitable for external AI services like ChatGPT
- Requires network security considerations

For detailed TCP server documentation, see [TCP Server Guide](tcp-server.md).

### Claude Desktop Configuration

Add the following to your Claude Desktop MCP configuration:

```json
{
  "mcpServers": {
    "gallagher": {
      "command": "python",
      "args": ["-m", "gallagher.mcp.server"],
      "env": {
        "GACC_API_KEY": "your-gallagher-api-key-here"
      }
    }
  }
}
```

### ChatGPT and External AI Services

For services that don't support subprocess-based MCP servers:

```bash
# Start TCP server
gala mcp serve --port 8080 --host 0.0.0.0
```

Then configure your AI service to connect to:

- **URL**: `http://your-server-ip:8080`
- **Protocol**: MCP over HTTP

### Other MCP Clients

For other MCP clients, you can run the server directly:

```bash
export GACC_API_KEY="your-gallagher-api-key-here"
python -m gallagher.mcp.server
```

## Available Tools

### list_cardholders

Lists all cardholders in the system.

**Parameters:**

- `limit` (integer, optional): Maximum number of cardholders to return (default: 100)
- `skip` (integer, optional): Number of cardholders to skip for pagination (default: 0)

**Example:**

```json
{
  "name": "list_cardholders",
  "arguments": {
    "limit": 10
  }
}
```

### search_cardholders

Searches for cardholders by name or other criteria.

**Parameters:**

- `name` (string, required): First or last name to search for
- `description` (string, optional): Keywords to search in description
- `division` (integer, optional): Division ID for hierarchical search
- `authorised_only` (boolean, optional): Only return authorised cardholders (default: false)
- `limit` (integer, optional): Maximum number of results to return (default: 100)
- `sort` (string, optional): Sort order - "id", "name", "-id", or "-name" (default: "name")

**Example:**

```json
{
  "name": "search_cardholders",
  "arguments": {
    "name": "John",
    "authorised_only": true,
    "limit": 5
  }
}
```

### get_cardholder

Gets detailed information about a specific cardholder.

**Parameters:**

- `id` (integer, required): Cardholder ID

**Example:**

```json
{
  "name": "get_cardholder",
  "arguments": {
    "id": 123
  }
}
```

### get_cardholder_cards

Gets all cards assigned to a specific cardholder.

**Parameters:**

- `id` (integer, required): Cardholder ID

**Example:**

```json
{
  "name": "get_cardholder_cards",
  "arguments": {
    "id": 123
  }
}
```

### get_cardholder_access_groups

Gets all access groups assigned to a specific cardholder.

**Parameters:**

- `id` (integer, required): Cardholder ID

**Example:**

```json
{
  "name": "get_cardholder_access_groups",
  "arguments": {
    "id": 123
  }
}
```

## Example Usage

Here's an example of how to use the MCP server programmatically:

```python
import asyncio
from gallagher.mcp.server import GallagherMCPServer

async def main():
    server = GallagherMCPServer()

    # List cardholders
    result = await server._list_cardholders({"limit": 5})
    print(result.content[0].text)

    # Search for cardholders
    result = await server._search_cardholders({
        "name": "John",
        "authorised_only": True
    })
    print(result.content[0].text)

asyncio.run(main())
```

## Error Handling

The MCP server handles various error conditions:

- **Authentication Error**: Occurs when the API key is invalid or missing
- **Not Found Error**: Occurs when a requested resource doesn't exist
- **Network Error**: Occurs when there are connectivity issues

All errors are returned as structured error responses with descriptive messages.

## Security Considerations

- The API key should be kept secure and not shared
- The server runs on stdio by default, which is secure for local use
- Consider using environment variables for API key storage
- The server only provides read access to cardholder data

## Troubleshooting

### Common Issues

1. **Authentication Error**: Ensure the `GACC_API_KEY` environment variable is set correctly
2. **Import Error**: Make sure all dependencies are installed
3. **Network Error**: Check your network connection and Gallagher Command Centre accessibility

### Testing

Use the built-in test command to verify functionality:

```bash
gala mcp test
```

This will test basic connectivity and cardholder operations.

## Development

The MCP server is built using the official MCP Python SDK and integrates with the existing Gallagher Command Centre API client. The server follows the MCP specification and provides a clean interface for AI assistants to query cardholder data.
