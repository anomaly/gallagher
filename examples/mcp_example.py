#!/usr/bin/env python3
"""Example usage of the Gallagher MCP Server

This script demonstrates how to use the Gallagher MCP server to query
cardholder information programmatically.

Usage:
    python examples/mcp_example.py

Make sure to set the GACC_API_KEY environment variable before running.
"""

from gallagher.mcp.server import GallagherMCPServer
import asyncio
import os
import sys
from typing import Dict, Any

# Add the parent directory to the path so we can import gallagher
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))


async def example_usage():
    """Demonstrate MCP server functionality"""

    # Check for API key
    if not os.environ.get("GACC_API_KEY"):
        print("Error: GACC_API_KEY environment variable is required")
        print("Please set your Gallagher Command Centre API key:")
        print("export GACC_API_KEY='your-api-key-here'")
        return

    print("Gallagher MCP Server Example")
    print("=" * 40)

    # Create server instance
    server = GallagherMCPServer()

    try:
        # Example 1: List cardholders
        print("\n1. Listing cardholders...")
        result = await server._list_cardholders({"limit": 5})
        print(result.content[0].text)

        # Example 2: Search for cardholders
        print("\n2. Searching for cardholders...")
        result = await server._search_cardholders({
            "name": "John",  # Replace with a name that exists in your system
            "limit": 3
        })
        print(result.content[0].text)

        # Example 3: Get detailed cardholder information
        # First, get a cardholder ID from the list
        list_result = await server._list_cardholders({"limit": 1})
        if "Found 0 cardholders" not in list_result.content[0].text:
            # Extract the first cardholder ID from the result
            lines = list_result.content[0].text.split('\n')
            for line in lines:
                if line.startswith("**ID:**"):
                    cardholder_id = int(line.split("**ID:**")[1].strip())
                    print(
                        f"\n3. Getting details for cardholder {cardholder_id}...")
                    detail_result = await server._get_cardholder({"id": cardholder_id})
                    print(detail_result.content[0].text)

                    # Example 4: Get cardholder cards
                    print(
                        f"\n4. Getting cards for cardholder {cardholder_id}...")
                    cards_result = await server._get_cardholder_cards({"id": cardholder_id})
                    print(cards_result.content[0].text)

                    # Example 5: Get cardholder access groups
                    print(
                        f"\n5. Getting access groups for cardholder {cardholder_id}...")
                    ag_result = await server._get_cardholder_access_groups({"id": cardholder_id})
                    print(ag_result.content[0].text)
                    break
        else:
            print("No cardholders found to demonstrate detailed queries")

        print("\nExample completed successfully!")

    except Exception as e:
        print(f"Error during example: {e}")
        print("Please check your API key and network connection.")


if __name__ == "__main__":
    asyncio.run(example_usage())
