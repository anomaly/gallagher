# Gallagher Python Toolkit

> The missing developer toolkit for Gallagher Command Centre

[![PyPI version](https://badge.fury.io/py/gallagher.svg)](https://badge.fury.io/py/gallagher)
[![Python Version](https://img.shields.io/pypi/pyversions/gallagher)](https://pypi.org/project/gallagher/)
[![Build Status](https://github.com/anomaly/gallagher/actions/workflows/run-tests.yml/badge.svg?branch=master)](https://github.com/anomaly/gallagher/actions?query=branch%3Amaster)

<div align="center">
<img src="https://raw.githubusercontent.com/anomaly/gallagher/master/assets/logo-gpt.png" alt="Gallagher Python Toolkit Logo" height=128 width=128/>
</div>

Gallagher Security manufacture a variety of perimeter [security products](https://security.gallagher.com). At the hear of these is the [Command Centre](https://products.security.gallagher.com/security/au/en_AU/products/software/command-centre/p/C201311) software. Command Centre is deployed locally (in simplistic terms, the complexity varies for every use case). Version `8.6` introduced a REST API which allows you to interact with the system via HTTP requests locally or via Gallagher's [Cloud API Gateway](https://gallaghersecurity.github.io/docs/Command%20Centre%20Cloud%20Api%20Gateway%20TIP.pdf) which eliminates the need for maintaining proxies and VPNs.

Our Python Toolkit focuses on enhancing the developer experience (DX) around the REST API. In principle we provide the following:

- **Python SDK** an idiomatic client (including `asyncio` support) to extend the CC functionality.
- **Command Line Interface** (CLI) to build powerful pipeline-based workflows.
- **Terminal User Interface** (TUI) for easy interactions with the Command Centre.
- **SQL interface** query the REST API as if it were a database or interact with via an ORM.

> [!NOTE]\
> This project is **NOT** affiliated with Gallagher Security. All trademarks are the property of their respective owners.

While Gallagher maintain a set of [Swagger definitions](https://github.com/gallaghersecurity/cc-rest-docs) for their API, they are primarily intended to generate the documentation [published on Github](https://gallaghersecurity.github.io/cc-rest-docs/ref/index.html). They use a tool called [Spectacle](https://github.com/sourcey/spectacle). Gallagher explicitly state that the Swagger definitions are not intended to be used to generate code. Due to this the API client is hand built and not auto-generated.

> [!IMPORTANT]\
> Due to custom annotations the YAML files will not parse with any standard parser.

Everything this project provides hinges upon our Python SDK, designed to enhance the developer experience. It's design is highly opinionated from our experience in building APIs, we ensure conformance with Gallagher software design interfaces.

> [!TIP]\
> If you've worked with [stripe-python](https://github.com/stripe/stripe-python) the syntax may feel familiar.

If you are using one of our user facing tools, it's not important for you to understand how the SDK works, however since it underpins everything, here's a rather sample example:

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
from gallagher.cc.cardholders import (
    Cardholder,
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

> [!IMPORTANT]\
> Gallagher infrastructure deals with perimeter security. We take this extremely seriously and providing a complete test suite to provide that our software meets all standards. These tests constantly run against our _demo_ command centre hosted on the cloud.

The rest of the README touches upon each of the tools we provide. If you like what you see so far we recommend you [head over to our documentation](https://anomaly.github.io/gallagher).

## Using the CLI and TUI

Our CLI is designed to automate custom workflows via scripts. Inspired by the greatest Unix tools out there, it does one thing and it does it well, leaving you to integrate it into a pipeline. The utility is able to speaking machine readable formats like JSON, YAML and CSV as well as producing formatted output.

Here's an example of fetching the details of a `cardholder`:

```
(gallagher-py3.11) ➜  gallagher git:(alpha-3) gala ch get 8272
 person
                  id 8272
          first_name Jerry
           last_name Zurcher
          short_name None
         description None
          authorised yes

  disable_cipher_pad no
            division 2
 hrefs
                edit edit
```

## Interacting via SQL

[Shillelagh](https://shillelagh.readthedocs.io/en/latest/) is a Python library that allows you to interact with REST APIs as if they were SQL databases, including the ability to provide a SQLAlchemy `dialect` allowing you to treat endpoints as a virtual table.

Assuming you had the SQL extensions installed, a simplistic example of querying Cardholders from the command would look like this:

```sql
🍀> SELECT * FROM "https://commandcentre-api-au.security.gallagher.cloud/api/cardholders" WHERE id=8427;
```

which would return a result set of:

```
first_name    last_name    authorised    id
------------  -----------  ------------ ----
Cammy         Albares      True         8427
(1 row in 0.23s)

```

## Command Centre API Notes

The Gallagher API the principles of [HATEOAS](https://en.wikipedia.org/wiki/HATEOAS) which ensures that the API is self-descriptive and future proof.

A `href` attribute provides a the destination of referenced objects in the responses. These are full qualified and will be prefixed with the server origin i.e if you are using the Cloud Gateway then all your URLs will be prefixed with the appropriate gateway's address.

These appear in various forms, starting from as simple as the `href` itself:

```json
"cardholders": {
    "href": "https://localhost:8904/api/access_groups/352/cardholders"
}
```

through to self recursive references (where the data is nested) with additional attributes:

```json
"parent": {
    "href": "https://localhost:8904/api/access_groups/100",
    "name": "All R&D"
}
```

> [!CAUTION]\
> Following the design patterns outlined by HATEOAS, you must never hardcode any URLs. You should hit the base API URL which returns the `hrefs` of all other resources.
> If you are using the Python SDK, then you don't have to worry about this, the client will handle this for you.

## Python SDK Design

This API client primarily depends on the following libraries:

- [httpx](https://www.python-httpx.org), fo transporting and parsing HTTP requests
- [pydantic](https://pydantic.dev), for validating responses and constructing request bodies

We use [Taskfile](https://taskfile.dev) to automate running tasks.

The project provides a comprehensive set of tests which can be run with `task test`. These tests do create objects in the Command Centre, we advice you to obtain a test license.

> [!IMPORTANT]
> It's **not recommended** to run tests against a production system.

### Data Transfer Objects

There are three types of schema definitions, each one of them suffixed with their intent:

- **Ref** are `References` to other objects, they using contain a `href` and possibly additional meta data such as a `name` or `id`
- **Summary** is what is returned by the Gallagher API in operations such as [searches](https://gallaghersecurity.github.io/cc-rest-docs/ref/cardholders.html), these are generally a subset of the full object
- **Detail** are the full object found at a particular `href`, they compound on the `Summary` schema and add additional attributes
- **Response** is a collection of `Summary` objects with other paths like `next` and `previous` for pagination and `updates` for polling results
- **Payload** is used to send a request to the API

In summary the properties of each are as follows:

- `Refs` are the minimal pathway to an object
- `Summary` builds on a `Ref` and provides a subset of the attributes
- `Detail` builds on a `Summary` and provides the full set of attributes
- `Response` encapsulates a collection of `Summary` objects, they typically have `next` and `previous` paths for pagination
- `Payload` are verbose and match the schema definition on the documentation

Each `resource` endpoint subclasses the `APIEndpoint` which marks a resource as `fetchable`, `queryable`, `creatable`, `updatable` and `deletable`. This is determined by the configuration defined using an `EndpointConfig` class.

> [!TIP]
> The above is meant to be a summary, please see [our documentation](https://anomaly.github.io/gallagher) for more details.

### Schema Design Patterns

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

where the `HrefMixin` (see also `OptionalHrefMixin` for use where the `href` is not always present) provides the `href` attribute:

```python
class HrefMixin(BaseModel):
    """ Href

    This mixin is used to define the href field for all
    responses from the Gallagher API.
    """
    href: str
```

These `Mixin` classes can also be used to declare attributes that seek to use the same pattern:

````python
class DivisionDetail(
    AppBaseModel,
    IdentityMixin,
):
    """ Defines a Division on the Gallagher Command Centre
    """

    name: str
    description: Optional[str] = None
    server_display_name: Optional[str] = None
    parent: OptionalHrefMixin = None

### Schemas

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
````

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
    """ Outlines the definition of a Division on the Gallagher Command Centre
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

## Resources

The following are resources that were discoverd during the design and development of these tools. Not all of them are in use by the toolkit, they were discovered as the library evolved.

### Python Libraries

> [!TIP]
> Following are Python libraries that I have found during the development of the Gallagher tools. They are not necessarily in use at the moment but a reference in case we need the functionality.

- [plotext](https://github.com/piccolomo/plotext?tab=readme-ov-file) - plots directly on your terminal (something I found when I was exploring apps like [dolphie](https://github.com/charles-001/dolphie))
- [rich-pixels](https://github.com/darrenburns/rich-pixels) - a [Rich-compatible](https://github.com/Textualize/rich) library for writing pixel images and other colourful grids to the terminal by @darrenburns
- [PyFilesystem](https://github.com/pyfilesystem/pyfilesystem2) - a Python file system abstraction layer

### Articles

- [A year of building for the terminal](https://textual.textualize.io/blog/2022/12/20/a-year-of-building-for-the-terminal/) by [@darrenburns](https://github.com/darrenburns)

## License

Distributed under the MIT License except Artwork and Branding assets.

## Credits

- [Matthew Skiles](https://matthewskiles.com) for the beautiful logo for the project.
- [Orion Edwards](https://github.com/borland) for all his support on getting @devraj started with the Gallagher API.
- [Mick Lambert](https://www.linkedin.com/in/michael-lambert-au/), [Tim Harris](https://www.linkedin.com/in/timharris01/), [Andrew Donkin](https://github.com/andrewdonkin), [Mike Margrain](https://www.linkedin.com/in/mike-margrain-b914381a/), [Nathan Matera](https://www.linkedin.com/in/nathan-matera-0a30b6240/) from the Gallagher team for all their support.
