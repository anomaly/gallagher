# Command Line Interface

> The CLI is developed using [Typer](https://typer.tiangolo.com) which builds on the [infamous](https://click.palletsprojects.com/en/8.1.x/)

Over the course of developing the Python idiomatic client for Gallagher, it became evident to us that the primary utility of the application will come from use facing tools that make the library immediately useful. This document outlines the scope of intent of the CLI and what feature it will provide (or initially anyway).

## Objectives

A big motivation for building this client library is efficiency in integrating Gallagher Command Centre into other systems. Integration primarily presents itself in the following forms:

- Querying the state of the Command Centre and reacting to the information
- Mutating the state of the system (e.g add a card holder, pass, access group, etc)
- Synchronizing the information back to ta local system (talked in detail about in [SQL](SQL.md))

While the API client is designed for structured programmatic access to the API, these use facing tools are designed to automate everyday use cases without needing to code.

## Audience

While the REST API client is aimed at developers (primarily Python developers) the CLI is intended for use by higher level uses for automation. The CLI still requires some technical knowledge and it targeted towards high level system integrator to build automation around the Gallagher ecosystem.

## Design

Following the [Unix philosophy](https://en.wikipedia.org/wiki/Unix_philosophy) of `Make each program do one thing well.` or summarised by [Peter H. Salus](https://en.wikipedia.org/wiki/Peter_H._Salus) as:

- Write programs that do one thing and do it well.
- Write programs to work together.
- Write programs to handle text streams, because that is a universal interface.

Each component presented by this project aims to do just that.

> The primary objective of the CLI is to interact with the JSON API through the command line so users can build high level automation without having to interact directly with the JSON payloads. It uses the Python API client to ensure strict data rules when interacting with the API endpoints, thus preventing corruption.

The project must provide complete documentation for the tool to be useful to an end user / system administrator.

## Scope

The initial version 

- Cardholder
- Visits
- Alarms



## Resources

- [Command Line Interface Guidelines - clig.dev](https://clig.dev)