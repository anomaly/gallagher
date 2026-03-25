# Command Line Interface

We provide a command line interface to interact with the Gallagher Command Centre. It uses the API client to communicate with the server, which doubly serves as a reference example of how to use the API client.

The CLI builds on [typer](https://typer.tiangolo.com) which in turn uses [click](https://click.palletsprojects.com). It also uses [rich](https://rich.readthedocs.io/en/stable/) to make the output nicer. The CLI is decoupled from the API client, and is not install by default.

The design follows the `git` like `command`, `sub-command` pattern, so it should feel quite familiar.

## Installation

If you are installing the SDK then `uv` will install the alias `gala` for you to interact with the CLI.

You can also use `pipx` to install the CLI directly from PyPI:

```bash
pipx install gallagher-sdk
```

## Usage

There are a few things to keep in mind while using the CLI, if you are lost you can always as for help:

```bash
gala --help
```

You can pass the configuration variables as command line options or as environment variables. The command line options take precedence over the environment variables.

```bash
gala --api-key YOUR_API_KEY --gateway US ch find devraj
```

alternatively if you had the environment variable `GACC_API_KEY` set you could do:

```bash
gala ch find devraj
```

> Remember: that the global command line options must precede the command and sub-command.


## CLI reference

The following is an auto-generated reference for the CLI commands and options and is kept upto date within the code itself.

::: mkdocs-typer2
    :module: gallagher.cli
    :name: app

## Resources

- [Command Line Interface Guidelines - clig.dev](https://clig.dev)
