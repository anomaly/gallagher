# Welcome to Gallagher Python Toolkit

Gallagher Python Toolkit aims to enhance the developer experience of working with Gallagher Security's Command Centre. Our why is as follows:

- We understand the technical requirements of Gallagher's API so you don't have to
- You write Python, we speak the underlying protocol
- A focus on security so we never exchange incorrect payloads
- Proof of quality by providing test suites

We currently provide the following:

- Python [idiomatic](https://www.merriam-webster.com/dictionary/idiomatic) client for developers
- Command line interface designed to build automations
- Terminal Inteface designed to provide a subset of the command centre functions, with a different viewpoint
- SQL interface (as a SQLAlchemy dialect) to ease integration into coprorate systems

> **Note:** This project is not affiliated with Gallagher in any way.

## Introduction

This project began by maintaining an idiomatic client for Python. The project began as a requirement for us to reliably work with the Gallagher API. While Gallagher publish their [API reference](https://gallaghersecurity.github.io/cc-rest-docs/ref/index.html) which is built from an OpenAPI spec with [Spectacle](https://github.com/sourcey/spectacle) documentation generator flavours. The OpenAPI spec is maintained by hand and [can be found on Github](https://github.com/GallagherSecurity/cc-rest-docs/tree/master/swagger).

Our assumption is that this is for security and technical reasons. In the spirit of building good quality software we embarked on building a Python idiomatic client with full test coverage.

The API client draws inspiration from companies like [Stripe](https://stripe.com) or projects like [pyndatic](https://pydantic.dev) who are known for stellar developer experience. Our aim is to provide a similar quality of developer experience for Gallagher projects.

The design pattern of the API client is opinionated from our experience as software engineers. We goto great lengths to document and justify our thought process so others can see where we are coming from.

## Features

- pydantic models for all API payloads
- HTTP transport using httpx
- Full test coverage
- A completely python based interface to interacting with Gallagher Command Centre

Additionally we offer:

- A command line interface to interact with the command centre
- A terminal user interface with some nifty features

