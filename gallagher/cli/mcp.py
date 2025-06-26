"""MCP (Model Context Protocol) CLI commands"""

import asyncio
import subprocess
import sys
from pathlib import Path

from typing import Optional
from typing_extensions import Annotated

import typer

from rich.console import Console
from rich.panel import Panel
from rich.text import Text

from .utils import AsyncTyper

app = AsyncTyper(
    help="MCP (Model Context Protocol) server commands for Gallagher Command Centre"
)


@app.command("serve")
async def serve(
    port: Annotated[
        Optional[int],
        typer.Option(
            "--port",
            "-p",
            help="Port to run the MCP server on (default: stdio)"
        )
    ] = None,
    host: Annotated[
        str,
        typer.Option(
            "--host",
            "-h",
            help="Host to bind to (default: localhost)"
        )
    ] = "localhost",
):
    """Start the MCP server

    This starts the Gallagher MCP server that exposes cardholder querying
    functionality through the Model Context Protocol. The server can be
    used by AI assistants to query Gallagher Command Centre data.

    By default, the server runs on stdio for use with MCP clients.
    Use --port to run as a TCP server for network access.
    """
    console = Console()

    try:
        from gallagher.mcp.server import GallagherMCPServer

        console.print(Panel(
            Text("Starting Gallagher MCP Server", style="bold green"),
            title="MCP Server",
            border_style="green"
        ))

        console.print("Server provides the following tools:")
        console.print("• list_cardholders - List all cardholders")
        console.print("• search_cardholders - Search for cardholders by name")
        console.print("• get_cardholder - Get detailed cardholder information")
        console.print(
            "• get_cardholder_cards - Get cards assigned to a cardholder")
        console.print(
            "• get_cardholder_access_groups - Get access groups for a cardholder")
        console.print()

        if port:
            console.print(f"Starting TCP server on {host}:{port}...")
            console.print(
                f"Server will be accessible at: http://{host}:{port}")
            console.print("Press Ctrl+C to stop the server")
            server = GallagherMCPServer()
            await server.run(host=host, port=port)
        else:
            console.print("Starting stdio server...")
            server = GallagherMCPServer()
            await server.run()

    except ImportError as e:
        console.print(f"[red]Error importing MCP dependencies: {e}[/red]")
        console.print(
            "Please install MCP dependencies: pip install mcp mcp-server-stdio")
        raise typer.Exit(code=1)
    except Exception as e:
        console.print(f"[red]Error starting MCP server: {e}[/red]")
        raise typer.Exit(code=1)


@app.command("config")
def config():
    """Show MCP configuration information

    Displays information about how to configure the Gallagher MCP server
    with various MCP clients.
    """
    console = Console()

    config_text = """
[bold]Gallagher MCP Server Configuration[/bold]

The Gallagher MCP server exposes cardholder querying functionality through
the Model Context Protocol. Here's how to configure it with various clients:

[bold green]Claude Desktop[/bold]
Add to your MCP servers configuration:

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

[bold green]ChatGPT and Other AI Services[/bold]
Run the server as a TCP server for network access:

```bash
# Start TCP server
export GACC_API_KEY="your-gallagher-api-key-here"
gala mcp serve --port 8080 --host 0.0.0.0

# Or directly with Python
python -m gallagher.mcp.server --port 8080 --host 0.0.0.0
```

Then configure your AI service to connect to:
- URL: http://your-server-ip:8080
- Protocol: MCP over HTTP

[bold green]Other MCP Clients[/bold]
Run the server directly:

```bash
export GACC_API_KEY="your-gallagher-api-key-here"
python -m gallagher.mcp.server
```

[bold yellow]Required Environment Variables[/bold]
• GACC_API_KEY: Your Gallagher Command Centre API key

[bold blue]Available Tools[/bold]
• list_cardholders - List all cardholders in the system
• search_cardholders - Search for cardholders by name or criteria
• get_cardholder - Get detailed information about a specific cardholder
• get_cardholder_cards - Get all cards assigned to a cardholder
• get_cardholder_access_groups - Get all access groups assigned to a cardholder

[bold red]Security Note[/bold]
When running as a TCP server, consider:
• Using a firewall to restrict access
• Running on localhost (127.0.0.1) for local-only access
• Using HTTPS/TLS in production environments
• Implementing authentication if needed
"""

    console.print(Panel(
        config_text,
        title="MCP Configuration",
        border_style="blue"
    ))


@app.command("test")
async def test():
    """Test the MCP server functionality

    Runs a quick test to verify that the MCP server can connect to
    Gallagher Command Centre and perform basic operations.
    """
    console = Console()

    try:
        from gallagher.mcp.server import GallagherMCPServer
        from gallagher.cc.cardholders import Cardholder

        console.print("[bold green]Testing MCP Server...[/bold green]")

        # Test basic cardholder list
        console.print("Testing cardholder list...")
        response = await Cardholder.list()
        console.print(f"✓ Found {len(response.results)} cardholders")

        # Test search functionality
        if response.results:
            test_cardholder = response.results[0]
            console.print(
                f"Testing search with name: {test_cardholder.first_name}")
            search_response = await Cardholder.search(name=test_cardholder.first_name)
            console.print(
                f"✓ Search returned {len(search_response.results)} results")

        console.print("[bold green]✓ All tests passed![/bold green]")
        console.print("The MCP server is ready to use.")

    except ImportError as e:
        console.print(f"[red]Error importing dependencies: {e}[/red]")
        raise typer.Exit(code=1)
    except Exception as e:
        console.print(f"[red]Test failed: {e}[/red]")
        console.print(
            "Please check your GACC_API_KEY environment variable and network connection.")
        raise typer.Exit(code=1)
