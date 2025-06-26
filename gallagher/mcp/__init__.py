"""MCP (Model Context Protocol) server for Gallagher Command Centre

This module provides an MCP server that exposes Gallagher Command Centre
functionality through the Model Context Protocol, allowing AI assistants
to query cardholders and other system data.
"""

from .server import GallagherMCPServer

__all__ = ["GallagherMCPServer"]
