# Gallagher Python Toolkit

Gallagher Security's Command Centre provides a REST API to programmatically interact with a large part of the system. This project maintains a set of developer focused tools to make integration experiences a delight. In addition we provide a set of power tools to make automations a breeze. At the moment we maintain:

- **Python SDK** an [idiomatic](https://www.merriam-webster.com/dictionary/idiomatic) client (featuring `asyncio`) to build applications for the Command Centre.
- **Command Line Interface** (CLI) to build powerful pipeline-based workflows.
- **Terminal User Interface** (TUI) for easy interactions with the Command Centre.
- **SQL interface** query the REST API like a database or interact with via an ORM.

> **Note:** While Anomaly is part of Gallagher's Technical Partner Program, this project is not officially affiliated with Gallagher.

## How to get started?

The offerings of this project are aimed at two significant groups of users:

- Software engineers who are looking to integrate Gallagher's technology into their systems
- Advanced users who are looking to automate their workflows

If you are a developer, the first things that might excite you are:

- [Python idiomatic client](./python-sdk.md) that adheres to the standards outlined by Gallagher
- [SQL interface to the REST API](./sql.md) that allows you to interact with the API using SQL queries

As an advanced user or integrator, we recommend at looking at:

- [Command line interface](./cli.md) that allows you to interact with the API from the terminal
- [Terminal interface](./tui.md) that provides a subset of the command centre functions in a different viewpoint

All of our tools are written using the Python programming languages. We provide binaries for most popular operating systems. If you are a developer and would like to contribute to the project, a good place to start is our [design document](./design.md).

## Motivation

Anomaly has a long history of working with APIs. In the early 2010s, during the early days of JSON APIs, we build a framework in Python called [prestans](https://github.com/anomaly/prestans/), it was designed to encompass the best practices of RESTful API design by providing a programmatic interface in Python. It allowed us to build large scale applications without losing quality as the team scaled up. `prestans` resulted in consistent code across the our applications.

prestans has since been superseded by projects like pydantic and FastAPI, but what we learnt from building it has stayed with us. We've taken our approach of deeply understanding the underlying protocol, design patterns and philosophy of the Gallagher API and encapsulated it as a set of developer products to empower others to build on top of their infrastructure.

Our central theme is that we do the heavily lifting so you can rely on the tools to build reliable integrations. This toolkit is the building block of one of our core business offerings, making it's quality a top priority for us.

## Background

Our initial requirements for interacting with Command Centre's API came from a prototype we built for a customer. Initially we interacted with the portion of the API that was relevant to our use case. Following a couple of iterations we decided to build a set of core offerings around Gallagher's technology.

Gallagher publish their [API reference](https://gallaghersecurity.github.io/cc-rest-docs/ref/index.html) which is built from an OpenAPI spec with [Spectacle](https://github.com/sourcey/spectacle) documentation generator flavours. The OpenAPI spec is maintained by hand and [can be found on Github](https://github.com/GallagherSecurity/cc-rest-docs/tree/master/swagger). While this is all you need to get started, it can be overwhelming to interact with the API directly.

Born out of solving our client's use cases, we built the Python client to interact with the API to ensure quality and achieve a great developer experience as our offerings scale. As our support requests grew it was evident that we could carve out a set of tools to enhance automation and integrations.

We believe that open sourcing these tools will result in a vibrant community of developers that will be able to leverage Gallagher's technology to build incredibly practical applications.

The API client draws inspiration from companies like [Stripe](https://stripe.com) or projects like [pyndatic](https://pydantic.dev) who are known for stellar developer experience. Our aim is to provide a similar quality of developer experience for Gallagher projects.

The design pattern of the API client is opinionated from our experience as software engineers. We goto great lengths to document and justify our thought process so others can see where we are coming from.
