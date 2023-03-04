# Gallagher Command Centre REST API Client
> Python idiomatic client for Gallagher Command Centre API

Gallagher Security manufacture a variety of [security products](https://security.gallagher.com) all of which are controlled by their [Command Centre](https://products.security.gallagher.com/security/au/en_AU/products/software/command-centre/p/C201311) software. Traditionally Command Centre has been a Windows based server product. Version `8.6` introduced a REST API which allows you to interact with the system via HTTP requests. Gallagher also provide a [Cloud API Gateway](https://gallaghersecurity.github.io/docs/Command%20Centre%20Cloud%20Api%20Gateway%20TIP.pdf) which allows third party integrations to securely communicate with the Command Centre on site.

This API client is a Python wrapper around their REST API and is designed to work locally or via the Cloud API Gateway.

While Gallagher maintain a set of [Swagger definitions](https://github.com/gallaghersecurity/cc-rest-docs) for their API, they are primarily intended to generate the documentation [published on Github](https://gallaghersecurity.github.io/cc-rest-docs/ref/index.html). They use a tool called [Spectacle](https://github.com/sourcey/spectacle). Gallagher explicitly state that the Swagger definitions are not intended to be used to generate code. Due to this the API client is hand built and not auto-generated.

> Due to custom annotations the YAML files will not parse with any standard parser.

The client was designed while building products around the Gallagher API. It's design is highly opinionated and does not conform with how Gallagher design software interfaces. If you've worked with [stripe-python](https://github.com/stripe/stripe-python) the syntax may feel familiar.

```python
from gallagher import cc, const

cc.api_key = "GH_"


cc.discover()
cc.Customer.create()
```

## Design

This API client primarily depends on the following libraries:

- [httpx](https://www.python-httpx.org), fo transporting and parsing HTTP requests
- [pydantic](https://pydantic.dev), for validating responses and constructing request bodies

We use [Taskfile](https://taskfile.dev) to automate running tasks.

The project provides a comprehensive set of tests which can be run with `task test`. These tests do create objects in the Command Centre, we advice you to obtain a test license. **DO NOT** run the tests against a production system.

## Configuring the Command Centre

The following requires you to have an understanding of the Gallagher Command Centre and how to configure it. If you are unsure, please contact your Gallagher representative.

Before you being, please ensure:

- You are running Command Centre version `8.60` or higher, older versions predate the gateway so cannot support it
- The gateway enabled at the system level
- If it is, has the gateway been enabled for your specific API key

To check the system level gateway status:

- Open the Command Centre Configuration Client
- From the `Configure` menu, select `Services and Workstations`
- Find the `Command Centre Cloud` item and double-click it
- Switch to the `Configuration` page, it should look something like this:

![Command Centre Cloud Configuration](assets/gallagher-command-centre-properties.png)

To check your API key:

- Open the Command Centre Configuration Client
- From the `Configure` menu, select `Services and Workstations`
- Find the item that represents your REST Client
- Switch to the `Connections` page, it should look something like this

![Command Centre Cloud Connections](assets/gallagher-rest-properties.png)

# License
Distributed under the MIT License.