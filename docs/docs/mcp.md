# MCP tools

[MCP (Model Context Protocol)](https://modelcontextprotocol.io/) is an open-source standard developed by Anthropic for connecting AI applications to external systems. 

Think of MCP like a USB-C port for AI applications. Just as USB-C provides a standardized way to connect electronic devices, MCP provides a standardized way to connect AI applications to external systems.

> Learn more in the [official documentation](https://modelcontextprotocol.io/docs/getting-started/intro).

This project provides a MCP server implementation using [the official Python SDK](https://github.com/modelcontextprotocol/python-sdk) which happens to play rather nicely with pydantic models, which is a core part of this project.

The three core concepts of MCP are:

- **Resources**: Structured data that can be queried and retrieved by AI applications e.g Cardholders, Events, Visits etc.
- **Tools**: Actions that can be performed on the external system, e.g `when did x cardholder last visit the premises?` or `create a mobile pass for y cardholder`.
- **Prompts**: Predefined text templates that can be used to guide AI applications in their interactions with the external system e.g `Generate a summary of the access history for cardholder x`.

This project generally provides the following MCP tools:

- **Sever**: a server that you can run to expose the MCP interface, this internally communicates with your Gallagher Command Centre instance via the REST API. It's ability will be restrcited by the permissions you assign to the API key.
- **Client**: a simple command line client that you can use to interact with the MCP server (or you can use the usual suspects like ChatGPT, Claude etc).

> Note: the client uses `pydantic-ai` and does rely on a model like `chatgpt`, you will need to supply an API key for the model you wish to use.

For the most of it the server should do what you would naturally expect from an agent, but feel free to read the [design section](#design) of this document to understand how it was specifically designed.

## Server

You will require to provide a REST API Key to the MCP Server. Do this by exporting the `GACC_API_KEY` environment variable before starting the server.

```bash 
export GACC_API_KEY="your_api_key_here"
uv run gala-mcp-server --host localhost --port 8000
```

For production you should serve this over HTTPS and behind a reverse proxy.


### Authentication

https://github.com/modelcontextprotocol/python-sdk?tab=readme-ov-file#authentication

## Client

## Design

Events:

- Search for events

Card Types:

- Find a card type

Access groups:

- Find an access group (this will be useful when giving a cardholder access)

Cardholder:

- Find a cardholder
- Show cardholder passes (tabular)

Vists:

- Find a visit

### Resources

This is a test

### Tools

### Prompts

[See Issue #70](https://github.com/anomaly/gallagher/issues/70) for original thoughts and discussion.


## Security