# Gallagher Python Toolkit

Gallagher Security manufacture a variety of perimeter [security products](https://security.gallagher.com). At the hear of these is the [Command Centre](https://products.security.gallagher.com/security/au/en_AU/products/software/command-centre/p/C201311) software. Command Centre is deployed locally (in simplistic terms, the complexity varies for every use case). Version `8.6` introduced a REST API which allows you to interact with the system via HTTP requests locally or via Gallagher's [Cloud API Gateway](https://gallaghersecurity.github.io/docs/Command%20Centre%20Cloud%20Api%20Gateway%20TIP.pdf) which eliminates the need for maintaining proxies and VPNs.

Our Python Toolkit focuses on enhancing the developer experience (DX) around the REST API. In principle we provide the following:

- **Python SDK** an idiomatic client (including `asyncio` support) to extend the CC functionality.
- **Command Line Interface** (CLI) to build powerful pipeline-based workflows.
- **Terminal User Interface** (TUI) for easy interactions with the Command Centre.
- **SQL interface** query the REST API as if it were a database or interact with via an ORM.

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

Gallagher publish their [API reference](https://gallaghersecurity.github.io/cc-rest-docs/ref/index.html) which is built from an OpenAPI spec with [Spectacle](https://github.com/sourcey/spectacle) documentation generator flavours. The OpenAPI spec is maintained by hand and [can be found on Github](https://github.com/GallagherSecurity/cc-rest-docs/tree/master/swagger).

While this is all you need to get started, it can be overwhelming to interact with the API directly.

Our Python Toolkit aims to encapsulate the design requirements of the API and provide a Python interface for you to build your integrations. Simply put:

> "You write Python, we speak REST to Gallagher's standards."

As we provided the viability of our commercial projects around Gallagher's infrastructure our support load went through the roof, the CLI, TUI and SQL interfaces are a formal expression of scripts, REST payload snippets that we used in the early days to perform tasks like adding cards to cardholders or keeping track of visits.

The API client draws inspiration from the works of [Stripe](https://stripe.com) or [pyndatic](https://pydantic.dev) who are known for providing a superb developer experience. Our aim is to provide a similar quality of developer experience for Gallagher projects.

While the entire project was built in self interest, we hope that many of you out there enjoy the developer experience if brings.

## Background

[Anomaly](https://www.anomaly.ltd) has a long history of working with APIs. In the early 2010s, during the early days of JSON APIs, we build a framework in Python called [prestans](https://github.com/anomaly/prestans/), it was designed to encompass the best practices of RESTful API design by providing a programmatic interface in Python. It allowed us to build large scale applications without losing quality as the team scaled up.

prestans has since been superseded by projects like pydantic and FastAPI, what we learnt from building it stayed with us. We've played on our strengths of deeply understanding the underlying protocol, design patterns and philosophy of the Gallagher API and encapsulated it as a set of developer products to empower others to build on top of their infrastructure.

Born out of solving our client's use cases, we built the Python client to interact with the API to ensure quality and achieve a great developer experience as our offerings scale. As our support requests grew it was evident that we could carve out a set of tools to enhance automation and integrations.

We believe that open sourcing these tools will result in a vibrant community of developers that will be able to leverage Gallagher's technology to build incredibly practical applications.

The design pattern of the API client is opinionated from our experience as software engineers. We goto great lengths to document our thought process and expression of the work we do. We look forward to your comments and feedback and can't wait to see what you build with our tools.
