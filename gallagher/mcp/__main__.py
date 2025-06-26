"""MCP Server entry point

This module allows running the Gallagher MCP server directly:

    python -m gallagher.mcp

This is equivalent to running the server through the CLI:

    gala mcp serve
"""

import asyncio
import os
import sys
import argparse

from .server import GallagherMCPServer


async def main():
    """Main entry point for the MCP server"""
    # Check for required environment variable
    if not os.environ.get("GACC_API_KEY"):
        print("Error: GACC_API_KEY environment variable is required", file=sys.stderr)
        print("Please set your Gallagher Command Centre API key:", file=sys.stderr)
        print("export GACC_API_KEY='your-api-key-here'", file=sys.stderr)
        sys.exit(1)

    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Gallagher MCP Server")
    parser.add_argument("--host", default="localhost",
                        help="Host to bind to (default: localhost)")
    parser.add_argument("--port", type=int,
                        help="Port to bind to (if not specified, uses stdio)")

    args = parser.parse_args()

    try:
        server = GallagherMCPServer()
        await server.run(host=args.host, port=args.port)
    except KeyboardInterrupt:
        print("Server stopped by user", file=sys.stderr)
        sys.exit(0)
    except Exception as e:
        print(f"Error running MCP server: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
