# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

This project uses [Taskfile](https://taskfile.dev) with `uv` as the Python package manager. Run all commands from the repo root.

```bash
# Run all tests (hits a live demo Command Centre via the cloud gateway)
task test

# Run a single test file
task test -- test_cardholder.py

# Run a single test by name
task test -- test_cardholder.py::test_cardholder_list

# List available tests
task test:list

# Lint
task lint

# Format
task black

# View coverage report (after running tests)
task test:coverreport

# Run TUI in dev mode
task dev:tui

# Run docs server
task dev:docs

# Run MCP server
task mcp:serve
```

Required environment variables (stored in `.env`, loaded by Taskfile):
- `GACC_API_KEY` — Gallagher Command Centre API key (8-segment format)
- `CERTIFICATE_ANOMALY` — TLS certificate contents (optional, for mTLS)
- `PRIVATE_KEY_ANOMALY` — TLS private key contents (optional, for mTLS)

Tests run against a live demo Command Centre. The `conftest.py` fixture randomly alternates between `GGL-API-KEY` and Basic authentication on each test run (since both are supported).

## Architecture

The toolkit is structured as five distinct layers that all build on the Python SDK:

```
gallagher/
  cc/          # Python SDK — API client and endpoint definitions
  dto/         # Data Transfer Objects (Pydantic models)
  cli/         # CLI (Typer-based, entry point: `gala`)
  tui/         # TUI (Textual-based, entry point: `gtui`)
  mcp/         # MCP server (FastMCP, entry point: `gala-mcp-server`)
  ext/         # Extensions (shillelagh SQL adapter)
```

### SDK layer (`gallagher/cc/`)

`APIClient` in `gallagher/cc/__init__.py` is the main entry point. On init it performs HATEOAS discovery by calling the root API endpoint, then instantiates each resource endpoint (e.g. `self.cardholders`, `self.doors`) passing the `CommandCentreConfig` and the `DiscoveryResponse`.

`CommandCentreConfig` (in `gallagher/cc/core.py`) is a `pydantic-settings` class that reads config from env vars or explicit arguments. Key fields: `api_key`, `api_base` (defaults to the AU cloud gateway), `file_tls_certificate`, `file_tls_key`, `use_basic_authentication`, `proxy`.

All resource endpoints inherit from `APIEndpoint` (in `gallagher/cc/core.py`) and implement `get_config() -> EndpointConfig`. `EndpointConfig` maps the HATEOAS-discovered hrefs to Pydantic DTO classes for list, retrieve, and follow operations. The base class provides `list()`, `retrieve()`, `search()`, `follow()`, `next()`, `previous()`, `_get()`, and `_post()` methods.

The `follow()` method implements Gallagher's long-poll pattern (30s server timeout, follow `next` href in a loop, stop via `asyncio.Event`).

### DTO layer (`gallagher/dto/`)

DTOs follow a strict hierarchy:
- **`Ref`** — minimal `href` + optional metadata (e.g. `name`)
- **`Summary`** — subset of attributes returned in list responses
- **`Detail`** — full object (extends Summary)
- **`Response`** — wraps a list of Summaries with pagination hrefs (`next`, `previous`, `updates`)
- **`Payload`** — used for POST/PATCH request bodies

All DTO classes inherit from `AppBaseModel` (in `gallagher/dto/utils.py`) which configures Pydantic to auto-translate between camelCase (API) and snake_case (Python). Core mixins: `HrefMixin`, `OptionalHrefMixin`, `IdentityMixin`, `OptionalIdentityMixin`.

`AppBaseResponseWithFollowModel` is the base for paginated responses and adds `next`, `previous`, and `updates` optional hrefs.

### CLI layer (`gallagher/cli/`)

Built with Typer. `gallagher/cli/__init__.py` wires the global callback (which initialises `APIClient`) and registers all sub-commands. Global options are passed via environment variables or CLI flags: `GACC_API_KEY`, `GACC_TLS_CERT`, `GACC_TLS_KEY`, `GACC_GATEWAY` (AU/US), `GACC_PROXY_URL`, `GACC_USE_BASIC_AUTH`. The `--format` flag supports `pretty`, `json`, `csv`, `markdown`. The `APIClient` instance is passed to subcommands via Typer's `click.Context`.

### MCP layer (`gallagher/mcp/`)

Implemented with FastMCP. The server (`gallagher/mcp/server/__init__.py`) reads credentials from environment variables, writes TLS material to temp files, and registers `@mcp.tool()` decorated async functions that call `api_client.*` methods.

### SQL extension (`gallagher/ext/shillelagh/`)

Provides a [shillelagh](https://github.com/betodealmeida/shillelagh) adapter (`CCAPIAdapter`) that lets SQL clients query API endpoints as virtual tables. Endpoints opt-in to SQL exposure via `__shillelagh__ = (EndpointClass,)` at the bottom of their module. Column types are derived dynamically from DTO annotations.

## Key conventions

- **Never hardcode URLs.** All endpoint hrefs come from HATEOAS discovery (`DiscoveryResponse`). The only hardcoded URLs are in `gallagher/const.py` (the gateway base URLs).
- **All endpoint calls are async** (`await api_client.cardholders.list()`). The CLI uses `AsyncTyper` to bridge Typer's sync interface.
- **Exceptions** in `gallagher/exception.py`: `UnlicensedFeatureException` (HTTP 403), `NotFoundException` (HTTP 404), `AuthenticationError` (HTTP 401), `DeadEndException` (no next/previous href), `PathFollowNotSupportedError`.
- **`__shillelagh__`** tuple at module level in endpoint files lists classes exposed as SQL virtual tables.
- **`pytest-asyncio`** is configured with `asyncio_mode = auto` so all async test functions are run automatically without decorators.
