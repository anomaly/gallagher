# TCP Server for AI Services

The Gallagher MCP server now supports running as a TCP server, making it accessible to AI services like ChatGPT, Claude, and other external applications that can connect via HTTP.

## Overview

The TCP server mode allows the Gallagher MCP server to:

- Run on a network port instead of stdio
- Accept connections from external AI services
- Provide the same cardholder querying functionality over HTTP
- Work with services that don't support subprocess-based MCP servers

## Quick Start

### 1. Set your API key

```bash
export GACC_API_KEY="your-gallagher-api-key-here"
```

### 2. Start the TCP server

```bash
# Using the CLI
gala mcp serve --port 8080 --host 0.0.0.0

# Or directly with Python
python -m gallagher.mcp.server --port 8080 --host 0.0.0.0
```

### 3. Connect from your AI service

Configure your AI service to connect to:

- **URL**: `http://your-server-ip:8080`
- **Protocol**: MCP over HTTP

## Configuration Options

### Host Binding

- `--host localhost` (default): Only accessible from the local machine
- `--host 0.0.0.0`: Accessible from any network interface
- `--host 192.168.1.100`: Bind to a specific IP address

### Port Selection

- Choose any available port (e.g., 8080, 3000, 5000)
- Avoid using privileged ports (below 1024)
- Ensure the port is not already in use

## Usage Examples

### Local Development

```bash
# Start server for local testing
gala mcp serve --port 8080 --host localhost
```

### Production Deployment

```bash
# Start server accessible from network
gala mcp serve --port 8080 --host 0.0.0.0
```

### Docker Deployment

```dockerfile
FROM python:3.10-slim

RUN pip install gallagher

EXPOSE 8080

CMD ["python", "-m", "gallagher.mcp.server", "--port", "8080", "--host", "0.0.0.0"]
```

## Available Tools

The TCP server provides the same tools as the stdio server:

- **list_cardholders** - List all cardholders in the system
- **search_cardholders** - Search for cardholders by name or criteria
- **get_cardholder** - Get detailed information about a specific cardholder
- **get_cardholder_cards** - Get all cards assigned to a cardholder
- **get_cardholder_access_groups** - Get all access groups assigned to a cardholder

## Testing the Server

### Using curl

```bash
# Test server connectivity
curl http://localhost:8080/health

# List available tools
curl -X POST http://localhost:8080/ \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "id": 1,
    "method": "tools/list",
    "params": {}
  }'
```

### Using the test script

```bash
python examples/tcp_server_test.py
```

## Security Considerations

### Network Security

- **Firewall**: Restrict access to the server port
- **Localhost only**: Use `--host localhost` for local-only access
- **VPN**: Use VPN for remote access
- **Reverse proxy**: Use nginx/apache with SSL termination

### Authentication

The current implementation relies on network-level security. For production use, consider:

- Implementing API key authentication
- Using HTTPS/TLS
- Adding rate limiting
- Implementing request validation

### Environment Variables

- Keep your `GACC_API_KEY` secure
- Use environment-specific configuration
- Consider using a secrets manager

## Troubleshooting

### Common Issues

1. **Port already in use**

   ```bash
   # Check what's using the port
   lsof -i :8080

   # Use a different port
   gala mcp serve --port 8081
   ```

2. **Connection refused**

   - Check if the server is running
   - Verify the host and port settings
   - Check firewall settings

3. **Authentication errors**
   - Verify `GACC_API_KEY` is set correctly
   - Check Gallagher Command Centre connectivity
   - Test with the stdio server first

### Debug Mode

```bash
# Run with verbose logging
python -m gallagher.mcp.server --port 8080 --host localhost
```

## Integration Examples

### ChatGPT Plugin

```json
{
  "name": "gallagher-mcp",
  "description": "Gallagher Command Centre integration",
  "endpoint": "http://localhost:8080",
  "protocol": "mcp"
}
```

### Custom AI Service

```python
import requests

# Connect to Gallagher MCP server
response = requests.post(
    "http://localhost:8080/",
    json={
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {
            "name": "list_cardholders",
            "arguments": {"limit": 10}
        }
    },
    headers={"Content-Type": "application/json"}
)

print(response.json())
```

## Performance Considerations

- The server handles one request at a time by default
- For high-load scenarios, consider running multiple instances
- Monitor memory usage with large cardholder datasets
- Use connection pooling for external Gallagher API calls

## Monitoring

### Health Check

```bash
curl http://localhost:8080/health
```

### Logs

Monitor server logs for:

- Connection attempts
- API call results
- Error messages
- Performance metrics

## Support

For issues with the TCP server:

1. Check the troubleshooting section above
2. Test with the stdio server first
3. Review the main MCP documentation
4. Check Gallagher Command Centre connectivity
