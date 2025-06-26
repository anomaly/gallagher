#!/usr/bin/env python3
"""Test script for Gallagher MCP TCP Server

This script demonstrates how to start and test the Gallagher MCP server
running on a TCP port for use with ChatGPT and other AI services.

Usage:
    python examples/tcp_server_test.py

Make sure to set the GACC_API_KEY environment variable before running.
"""

import asyncio
import os
import sys
import time
import requests
import json
from typing import Dict, Any

# Add the parent directory to the path so we can import gallagher
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))


async def test_tcp_server():
    """Test the TCP server functionality"""

    # Check for API key
    if not os.environ.get("GACC_API_KEY"):
        print("Error: GACC_API_KEY environment variable is required")
        print("Please set your Gallagher Command Centre API key:")
        print("export GACC_API_KEY='your-api-key-here'")
        return

    print("Gallagher MCP TCP Server Test")
    print("=" * 40)

    # Configuration
    host = "localhost"
    port = 8080
    base_url = f"http://{host}:{port}"

    # Start the server in the background
    print(f"Starting TCP server on {host}:{port}...")

    # Import and start server
    from gallagher.mcp.server import GallagherMCPServer

    server = GallagherMCPServer()

    # Start server in background task
    server_task = asyncio.create_task(server.run(host=host, port=port))

    # Wait a moment for server to start
    await asyncio.sleep(2)

    try:
        # Test basic connectivity
        print(f"Testing connectivity to {base_url}...")
        response = requests.get(f"{base_url}/health", timeout=5)
        print(f"✓ Server is responding (status: {response.status_code})")

        # Test MCP protocol
        print("Testing MCP protocol...")

        # Test list_tools
        tools_request = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "tools/list",
            "params": {}
        }

        response = requests.post(
            f"{base_url}/",
            json=tools_request,
            headers={"Content-Type": "application/json"},
            timeout=10
        )

        if response.status_code == 200:
            result = response.json()
            if "result" in result and "tools" in result["result"]:
                tools = result["result"]["tools"]
                print(f"✓ Server returned {len(tools)} tools:")
                for tool in tools:
                    print(f"  - {tool['name']}: {tool['description']}")
            else:
                print("⚠ Server responded but no tools found")
        else:
            print(f"✗ Server returned error: {response.status_code}")
            print(f"Response: {response.text}")

    except requests.exceptions.ConnectionError:
        print("✗ Could not connect to server")
        print("Make sure the server is running and the port is accessible")
    except Exception as e:
        print(f"✗ Error testing server: {e}")
    finally:
        # Stop the server
        print("Stopping server...")
        server_task.cancel()
        try:
            await server_task
        except asyncio.CancelledError:
            pass
        print("Server stopped")


def start_server_demo():
    """Demonstrate how to start the server for external use"""
    print("\n" + "=" * 50)
    print("SERVER DEMO MODE")
    print("=" * 50)
    print("To start the server for external AI services:")
    print()
    print("1. Set your API key:")
    print("   export GACC_API_KEY='your-api-key-here'")
    print()
    print("2. Start the server:")
    print("   gala mcp serve --port 8080 --host 0.0.0.0")
    print()
    print("3. Or start directly with Python:")
    print("   python -m gallagher.mcp.server --port 8080 --host 0.0.0.0")
    print()
    print("4. Configure your AI service to connect to:")
    print("   http://your-server-ip:8080")
    print()
    print("Available tools:")
    print("- list_cardholders")
    print("- search_cardholders")
    print("- get_cardholder")
    print("- get_cardholder_cards")
    print("- get_cardholder_access_groups")
    print()
    print("Press Ctrl+C to stop the server when done")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "demo":
        start_server_demo()
    else:
        asyncio.run(test_tcp_server())
