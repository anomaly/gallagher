# Gallagher Python Toolkit

> Python idiomatic REST API client, a command line interface and a text based console for Gallagher Command Centre API

Gallagher Security manufacture a variety of [security products](https://security.gallagher.com) all of which are controlled by their [Command Centre](https://products.security.gallagher.com/security/au/en_AU/products/software/command-centre/p/C201311) software. Traditionally Command Centre has been a Windows based server product. Version `8.6` introduced a REST API which allows you to interact with the system via HTTP requests. Gallagher also provide a [Cloud API Gateway](https://gallaghersecurity.github.io/docs/Command%20Centre%20Cloud%20Api%20Gateway%20TIP.pdf) which allows third party integrations to securely communicate with the Command Centre on site.

This API client is a Python wrapper around their REST API and is designed to work locally or via the Cloud API Gateway.

While Gallagher maintain a set of [Swagger definitions](https://github.com/gallaghersecurity/cc-rest-docs) for their API, they are primarily intended to generate the documentation [published on Github](https://gallaghersecurity.github.io/cc-rest-docs/ref/index.html). They use a tool called [Spectacle](https://github.com/sourcey/spectacle). Gallagher explicitly state that the Swagger definitions are not intended to be used to generate code. Due to this the API client is hand built and not auto-generated.

> Due to custom annotations the YAML files will not parse with any standard parser.

The client was designed while building products around the Gallagher API. It's design is highly opinionated and does not conform with how Gallagher design software interfaces. If you've worked with [stripe-python](https://github.com/stripe/stripe-python) the syntax may feel familiar.

```python
# Import core python libs
import os
import asyncio

# Import the client and models
from gallagher import (
    cc,
)
from gallagher.dto.summary import (
    CardholderSummary,
)
from gallagher.cc.cardholders.cardholders import (
    Cardholder
)

# Set the API key from the environment
api_key = os.environ.get("GACC_API_KEY")
cc.api_key = api_key

# Async support gives us back a coroutine
ch_coro = Cardholder.list()

# Run the coroutine to get the cardholder
cardholders = asyncio.run(ch_coro)
cardholder = cardholders.results[0]

# This is now a pydantic object
type(cardholder) == CardholderSummary

# Print out some details from the object
cardholder.href
cardholder.first_name
```

> Note this project is **NOT** officially affiliated with Gallagher Security

## API Notes

The Gallagher API uses `href` attributes to provide a the destination of referenced objects in the responses. These are prefixed with the server origin i.e if you are using the Cloud Gateway then all your URLs will be prefixed with the appropriate gateway's address.

These appear in various forms, starting from as simple as the `href` itself:

```json
"cardholders": {
    "href": "https://localhost:8904/api/access_groups/352/cardholders"
}
```

through to self recursive references with additional attributes:

```json
"parent": {
    "href": "https://localhost:8904/api/access_groups/100",
    "name": "All R&D"
}
```

> Above examples have been taken from the Gallagher documentation

Our `schemas` provide a set of `Mixins` that are used to construct the Models. These are repeatable patterns that need not be repeated. The typical patter would be to subclass from the `Mixins` e.g:

```python
from .utils import AppBaseModel, IdentityMixin, HrefMixin

class AccessGroupRef(
    AppBaseModel,
    HrefMixin
):
    """ Access Groups is what a user is assigned to to provide access to doors
    """
    name: str
```

where the `HrefMixin` provides the `href` attribute:

```python
class HrefMixin(BaseModel):
    """ Href

    This mixin is used to define the href field for all
    responses from the Gallagher API.
    """
    href: str
```

These `Mixin` classes can also be used to declare attributes that seek to use the same pattern:

```python
class DivisionDetail(
    AppBaseModel,
    IdentityMixin,
):
    """
    """

    name: str
    description: Optional[str]
    server_display_name: str
    parent: Optional[HrefMixin]
```

where `parent` is simply an `href` without any other attributes. In the cases where these attributes have more than just an `href` we defined `Reference` classes:

```python
class AccessGroupRef(
    AppBaseModel,
    HrefMixin
):
    """ Access Groups is what a user is assigned to to provide access to doors
    """
    name: str
```

and use them to populate the attributes:

```python
class VisitorTypeDetail(
    AppBaseModel,
    IdentityMixin
):
    """
    """
    access_group : AccessGroupRef
    host_access_groups: list[AccessGroupSummary]
    visitor_access_groups: list[AccessGroupSummary]
```

In this example the `AppGroupRef` has a `name` attribute which is not present in the `HrefMixin` class.

> Please see the schema section for naming conventions for `schema` classes

## Design

This API client primarily depends on the following libraries:

- [httpx](https://www.python-httpx.org), fo transporting and parsing HTTP requests
- [pydantic](https://pydantic.dev), for validating responses and constructing request bodies

We use [Taskfile](https://taskfile.dev) to automate running tasks.

The project provides a comprehensive set of tests which can be run with `task test`. These tests do create objects in the Command Centre, we advice you to obtain a test license.

> It's **not recommended** to run tests against a production system.

### Data Transfer Objects

There are three types of schema definitions, each one of them suffixed with their intent:

- **Ref** are `References` to other objects, they using contain a `href` and possibly additional meta data such as a `name` or `id`
- **Summary** is what is returned by the Gallagher API in operations such as [searches](https://gallaghersecurity.github.io/cc-rest-docs/ref/cardholders.html), these are generally a subset of the full object
- **Detail** are the full object found at a particular `href`, they compound on the `Summary` schema and add additional attributes

In summary:

- `Refs` are the minimal pathway to an object
- `Summary` builds on a `Ref` and provides a subset of the attributes
- `Detail` builds on a `Summary` and provides the full set of attributes

### Resources

Resources are `fetchable`, `queryable`, `creatable`, `updatable` and `deletable`.

### Responses

Responses can be the object itself or a response layout

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

![Command Centre Cloud Configuration](https://raw.githubusercontent.com/anomaly/gallagher/master/assets/gallagher-command-centre-properties.png)

To check your API key:

- Open the Command Centre Configuration Client
- From the `Configure` menu, select `Services and Workstations`
- Find the item that represents your REST Client
- Switch to the `Connections` page, it should look something like this

![Command Centre Cloud Connections](https://raw.githubusercontent.com/anomaly/gallagher/master/assets/gallagher-rest-properties.png)

## Python Libraries

> Following are Python libraries that I have found during the development of the Gallagher tools. They are not necessarily in use at the moment but a reference in case we need the functionality.

- [plotext](https://github.com/piccolomo/plotext?tab=readme-ov-file) - plots directly on your terminal (something I found when I was exploring apps like [dolphie](https://github.com/charles-001/dolphie))
- [rich-pixels](https://github.com/darrenburns/rich-pixels) - a [Rich-compatible](https://github.com/Textualize/rich) library for writing pixel images and other colourful grids to the terminal by @darrenburns
- [PyFilesystem](https://github.com/pyfilesystem/pyfilesystem2) - a Python file system abstraction layer

### Articles

- [A year of building for the terminal](https://textual.textualize.io/blog/2022/12/20/a-year-of-building-for-the-terminal/) by @darrenburns

## License

Distributed under the MIT License.
