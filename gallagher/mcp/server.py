"""Gallagher MCP Server implementation"""

import asyncio
import json
import socket
from typing import Any, Dict, List, Optional, Sequence
from datetime import datetime

from mcp.server import Server, NotificationOptions
from mcp.server.models import InitializationOptions
from mcp.server.stdio import stdio_server
from mcp.server.streamable_http import StreamableHTTPServerTransport
from mcp.types import (
    CallToolRequest,
    CallToolResult,
    ListToolsRequest,
    ListToolsResult,
    Tool,
    TextContent,
    ImageContent,
    EmbeddedResource,
    LoggingLevel,
)

from ..cc.cardholders import Cardholder
from ..dto.detail import CardholderDetail
from ..dto.response import CardholderSummaryResponse
from ..dto.summary import CardholderSummary
from ..enum import SearchSortOrder
from ..exception import NotFoundException, AuthenticationError


class GallagherMCPServer:
    """MCP Server for Gallagher Command Centre"""

    def __init__(self):
        self.server = Server("gallagher")
        self._setup_tools()

    def _setup_tools(self):
        """Setup all available tools"""

        @self.server.list_tools()
        async def handle_list_tools() -> ListToolsResult:
            """List all available tools"""
            return ListToolsResult(
                tools=[
                    Tool(
                        name="list_cardholders",
                        description="List all cardholders in the system",
                        inputSchema={
                            "type": "object",
                            "properties": {
                                "limit": {
                                    "type": "integer",
                                    "description": "Maximum number of cardholders to return (default: 100)",
                                    "default": 100
                                },
                                "skip": {
                                    "type": "integer",
                                    "description": "Number of cardholders to skip (for pagination)",
                                    "default": 0
                                }
                            }
                        }
                    ),
                    Tool(
                        name="search_cardholders",
                        description="Search for cardholders by name or other criteria",
                        inputSchema={
                            "type": "object",
                            "properties": {
                                "name": {
                                    "type": "string",
                                    "description": "First or last name to search for"
                                },
                                "description": {
                                    "type": "string",
                                    "description": "Keywords to search in description"
                                },
                                "division": {
                                    "type": "integer",
                                    "description": "Division ID for hierarchical search"
                                },
                                "authorised_only": {
                                    "type": "boolean",
                                    "description": "Only return authorised cardholders",
                                    "default": False
                                },
                                "limit": {
                                    "type": "integer",
                                    "description": "Maximum number of results to return",
                                    "default": 100
                                },
                                "sort": {
                                    "type": "string",
                                    "enum": ["id", "name", "-id", "-name"],
                                    "description": "Sort order for results",
                                    "default": "name"
                                }
                            },
                            "required": ["name"]
                        }
                    ),
                    Tool(
                        name="get_cardholder",
                        description="Get detailed information about a specific cardholder",
                        inputSchema={
                            "type": "object",
                            "properties": {
                                "id": {
                                    "type": "integer",
                                    "description": "Cardholder ID"
                                }
                            },
                            "required": ["id"]
                        }
                    ),
                    Tool(
                        name="get_cardholder_cards",
                        description="Get all cards assigned to a specific cardholder",
                        inputSchema={
                            "type": "object",
                            "properties": {
                                "id": {
                                    "type": "integer",
                                    "description": "Cardholder ID"
                                }
                            },
                            "required": ["id"]
                        }
                    ),
                    Tool(
                        name="get_cardholder_access_groups",
                        description="Get all access groups assigned to a specific cardholder",
                        inputSchema={
                            "type": "object",
                            "properties": {
                                "id": {
                                    "type": "integer",
                                    "description": "Cardholder ID"
                                }
                            },
                            "required": ["id"]
                        }
                    )
                ]
            )

        @self.server.call_tool()
        async def handle_call_tool(name: str, arguments: Dict[str, Any]) -> CallToolResult:
            """Handle tool calls"""

            try:
                if name == "list_cardholders":
                    return await self._list_cardholders(arguments)
                elif name == "search_cardholders":
                    return await self._search_cardholders(arguments)
                elif name == "get_cardholder":
                    return await self._get_cardholder(arguments)
                elif name == "get_cardholder_cards":
                    return await self._get_cardholder_cards(arguments)
                elif name == "get_cardholder_access_groups":
                    return await self._get_cardholder_access_groups(arguments)
                else:
                    return CallToolResult(
                        content=[
                            TextContent(
                                type="text",
                                text=f"Unknown tool: {name}"
                            )
                        ],
                        isError=True
                    )

            except AuthenticationError as e:
                return CallToolResult(
                    content=[
                        TextContent(
                            type="text",
                            text=f"Authentication error: {str(e)}. Please ensure the GACC_API_KEY environment variable is set correctly."
                        )
                    ],
                    isError=True
                )
            except NotFoundException as e:
                return CallToolResult(
                    content=[
                        TextContent(
                            type="text",
                            text=f"Not found: {str(e)}"
                        )
                    ],
                    isError=True
                )
            except Exception as e:
                return CallToolResult(
                    content=[
                        TextContent(
                            type="text",
                            text=f"Error: {str(e)}"
                        )
                    ],
                    isError=True
                )

    async def _list_cardholders(self, arguments: Dict[str, Any]) -> CallToolResult:
        """List all cardholders"""
        limit = arguments.get("limit", 100)
        skip = arguments.get("skip", 0)

        try:
            response = await Cardholder.list(skip=skip)

            # Limit results if needed
            cardholders = response.results[:limit]

            # Format the results
            result_text = f"Found {len(cardholders)} cardholders:\n\n"

            for cardholder in cardholders:
                result_text += f"**ID:** {cardholder.id}\n"
                result_text += f"**Name:** {cardholder.first_name} {cardholder.last_name}\n"
                result_text += f"**Authorised:** {'Yes' if cardholder.authorised else 'No'}\n"
                if cardholder.description:
                    result_text += f"**Description:** {cardholder.description}\n"
                result_text += "---\n"

            return CallToolResult(
                content=[
                    TextContent(
                        type="text",
                        text=result_text
                    )
                ]
            )

        except Exception as e:
            return CallToolResult(
                content=[
                    TextContent(
                        type="text",
                        text=f"Error listing cardholders: {str(e)}"
                    )
                ],
                isError=True
            )

    async def _search_cardholders(self, arguments: Dict[str, Any]) -> CallToolResult:
        """Search for cardholders"""
        name = arguments.get("name")
        description = arguments.get("description")
        division = arguments.get("division")
        authorised_only = arguments.get("authorised_only", False)
        limit = arguments.get("limit", 100)
        sort_str = arguments.get("sort", "name")

        # Convert sort string to enum
        sort_map = {
            "id": SearchSortOrder.ID,
            "name": SearchSortOrder.NAME,
            "-id": SearchSortOrder.ID_DESC,
            "-name": SearchSortOrder.NAME_DESC
        }
        sort = sort_map.get(sort_str, SearchSortOrder.NAME)

        try:
            response = await Cardholder.search(
                name=name,
                description=description,
                division=division,
                top=limit,
                sort=sort
            )

            # Filter by authorised status if requested
            cardholders = response.results
            if authorised_only:
                cardholders = [c for c in cardholders if c.authorised]

            # Format the results
            result_text = f"Found {len(cardholders)} cardholders matching search criteria:\n\n"

            for cardholder in cardholders:
                result_text += f"**ID:** {cardholder.id}\n"
                result_text += f"**Name:** {cardholder.first_name} {cardholder.last_name}\n"
                result_text += f"**Authorised:** {'Yes' if cardholder.authorised else 'No'}\n"
                if cardholder.description:
                    result_text += f"**Description:** {cardholder.description}\n"
                result_text += "---\n"

            return CallToolResult(
                content=[
                    TextContent(
                        type="text",
                        text=result_text
                    )
                ]
            )

        except Exception as e:
            return CallToolResult(
                content=[
                    TextContent(
                        type="text",
                        text=f"Error searching cardholders: {str(e)}"
                    )
                ],
                isError=True
            )

    async def _get_cardholder(self, arguments: Dict[str, Any]) -> CallToolResult:
        """Get detailed information about a specific cardholder"""
        cardholder_id = arguments.get("id")

        if not cardholder_id:
            return CallToolResult(
                content=[
                    TextContent(
                        type="text",
                        text="Cardholder ID is required"
                    )
                ],
                isError=True
            )

        try:
            cardholder = await Cardholder.retrieve(cardholder_id)

            # Format the detailed information
            result_text = f"**Cardholder Details**\n\n"
            result_text += f"**ID:** {cardholder.id}\n"
            result_text += f"**Name:** {cardholder.first_name} {cardholder.last_name}\n"
            if cardholder.short_name:
                result_text += f"**Short Name:** {cardholder.short_name}\n"
            if cardholder.description:
                result_text += f"**Description:** {cardholder.description}\n"
            result_text += f"**Authorised:** {'Yes' if cardholder.authorised else 'No'}\n"
            result_text += f"**Division:** {cardholder.division.id} - {cardholder.division.name}\n"

            if cardholder.last_successful_access_time:
                result_text += f"**Last Access:** {cardholder.last_successful_access_time}\n"

            if cardholder.last_successful_access_zone:
                result_text += f"**Last Access Zone:** {cardholder.last_successful_access_zone.name}\n"

            result_text += f"\n**Cards:** {len(cardholder.cards)}\n"
            result_text += f"**Access Groups:** {len(cardholder.access_groups)}\n"
            result_text += f"**Personal Data Fields:** {len(cardholder.personal_data_definitions)}\n"

            # Add personal data if available
            if cardholder.personal_data_definitions:
                result_text += "\n**Personal Data:**\n"
                for pdf in cardholder.personal_data_definitions:
                    result_text += f"- {pdf.name}: {pdf.contents}\n"

            return CallToolResult(
                content=[
                    TextContent(
                        type="text",
                        text=result_text
                    )
                ]
            )

        except Exception as e:
            return CallToolResult(
                content=[
                    TextContent(
                        type="text",
                        text=f"Error retrieving cardholder: {str(e)}"
                    )
                ],
                isError=True
            )

    async def _get_cardholder_cards(self, arguments: Dict[str, Any]) -> CallToolResult:
        """Get all cards assigned to a specific cardholder"""
        cardholder_id = arguments.get("id")

        if not cardholder_id:
            return CallToolResult(
                content=[
                    TextContent(
                        type="text",
                        text="Cardholder ID is required"
                    )
                ],
                isError=True
            )

        try:
            cardholder = await Cardholder.retrieve(cardholder_id)

            result_text = f"**Cards for {cardholder.first_name} {cardholder.last_name}**\n\n"

            if not cardholder.cards:
                result_text += "No cards assigned to this cardholder.\n"
            else:
                for i, card in enumerate(cardholder.cards, 1):
                    result_text += f"**Card {i}:**\n"
                    result_text += f"- **Number:** {card.number}\n"
                    if card.card_serial_number:
                        result_text += f"- **Serial Number:** {card.card_serial_number}\n"
                    result_text += f"- **Type:** {card.type.name}\n"
                    result_text += f"- **Status:** {card.status.value}\n"
                    result_text += f"- **Credential Class:** {card.credential_class.value}\n"

                    if card.valid_from:
                        result_text += f"- **Valid From:** {card.valid_from}\n"
                    if card.valid_until:
                        result_text += f"- **Valid Until:** {card.valid_until}\n"

                    if card.pin:
                        result_text += f"- **PIN:** {card.pin}\n"

                    result_text += "---\n"

            return CallToolResult(
                content=[
                    TextContent(
                        type="text",
                        text=result_text
                    )
                ]
            )

        except Exception as e:
            return CallToolResult(
                content=[
                    TextContent(
                        type="text",
                        text=f"Error retrieving cardholder cards: {str(e)}"
                    )
                ],
                isError=True
            )

    async def _get_cardholder_access_groups(self, arguments: Dict[str, Any]) -> CallToolResult:
        """Get all access groups assigned to a specific cardholder"""
        cardholder_id = arguments.get("id")

        if not cardholder_id:
            return CallToolResult(
                content=[
                    TextContent(
                        type="text",
                        text="Cardholder ID is required"
                    )
                ],
                isError=True
            )

        try:
            cardholder = await Cardholder.retrieve(cardholder_id)

            result_text = f"**Access Groups for {cardholder.first_name} {cardholder.last_name}**\n\n"

            if not cardholder.access_groups:
                result_text += "No access groups assigned to this cardholder.\n"
            else:
                for i, ag in enumerate(cardholder.access_groups, 1):
                    result_text += f"**Access Group {i}:**\n"
                    result_text += f"- **Name:** {ag.access_group.name}\n"
                    result_text += f"- **Status:** {ag.status.value}\n"

                    if ag.valid_from:
                        result_text += f"- **Valid From:** {ag.valid_from}\n"
                    if ag.valid_until:
                        result_text += f"- **Valid Until:** {ag.valid_until}\n"

                    result_text += "---\n"

            return CallToolResult(
                content=[
                    TextContent(
                        type="text",
                        text=result_text
                    )
                ]
            )

        except Exception as e:
            return CallToolResult(
                content=[
                    TextContent(
                        type="text",
                        text=f"Error retrieving cardholder access groups: {str(e)}"
                    )
                ],
                isError=True
            )

    async def run(self, host: str = "localhost", port: Optional[int] = None):
        """Run the MCP server

        Args:
            host: Host to bind to (default: localhost)
            port: Port to bind to (if None, uses stdio)
        """
        if port is not None:
            # Run as TCP server
            transport = StreamableHTTPServerTransport()
            await transport.run_server(
                self.server,
                host=host,
                port=port,
                initialization_options=InitializationOptions(
                    server_name="gallagher-mcp",
                    server_version="1.0.0",
                    capabilities=self.server.get_capabilities(
                        notification_options=NotificationOptions(
                            prompts_changed=False,
                            resources_changed=False,
                            tools_changed=False,
                        ),
                        experimental_capabilities=None,
                    ),
                ),
            )
        else:
            # Run as stdio server (default)
            async with stdio_server() as (read_stream, write_stream):
                await self.server.run(
                    read_stream,
                    write_stream,
                    InitializationOptions(
                        server_name="gallagher-mcp",
                        server_version="1.0.0",
                        capabilities=self.server.get_capabilities(
                            notification_options=NotificationOptions(
                                prompts_changed=False,
                                resources_changed=False,
                                tools_changed=False,
                            ),
                            experimental_capabilities=None,
                        ),
                    ),
                )


async def main():
    """Main entry point for the MCP server"""
    import argparse

    parser = argparse.ArgumentParser(description="Gallagher MCP Server")
    parser.add_argument("--host", default="localhost",
                        help="Host to bind to (default: localhost)")
    parser.add_argument("--port", type=int,
                        help="Port to bind to (if not specified, uses stdio)")

    args = parser.parse_args()

    server = GallagherMCPServer()
    await server.run(host=args.host, port=args.port)


if __name__ == "__main__":
    asyncio.run(main())
