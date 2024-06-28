# Contribution's Manual

The following guide is aimed at developers who are looking to understand the toolkit at a deeper level or wish to contribute to the project. The aim is to outline the design thinking behind various components of the project.

## Layout

It's handy to know where each portion of the project lives, so you can find your way around. Majority of the source is located under the `gallagher` directory, which is what is shipped via `pypi`. `tests` are not part of the distribution and `examples` are intended to be runnable examples a developer can copy and paste.

```
.
├── assets                          assets for the github/pypi project
├── docs                            documentation via mkdocs
│   └── docs                        where the markdown files are stored
├── examples                        examples of how to use the API client
├── gallagher                       the main package
│   ├── cc
│   │   ├── alarms                  alarms endpoint
│   │   ├── cardholders             cardholders endpoint
│   │   └── status_overrides        status overrides endpoint
│   ├── cli                         command line interface
│   ├── tui                         terminal user interface
│   ├── dto                         data transfer objects
│   │   ├── detail                  detail objects
│   │   ├── payload                 payloads for requests
│   │   ├── ref                     reference objects
│   │   ├── response                response objects
│   │   └── summary                 summary objects
│   └── ext                         extensions to the core package e.g SQL
└── tests                           tests for the project
```

## Toolchain

Majority of the development was conducted on macOS, but the toolchain should be compatible with any operating system. All elements of the project were developed in `python` with standard tooling. Our major dependencies are `httpx` and `pydantic`.

In addition to the usual suspects (e.g pytest) we use:

- `task` - as the task runner of choice, it's widely available on platforms and supports Github actions. All endpoints are documented within the command line tool.
- `poetry` as our package manager of choice for the python project
- `mkdocs` for documentation, maintained using markdown

## SDK

A central feature to this project is the API client, focused on a superior developer experience and performance we spent substantial time in designing the Python interface to ensure it scales. We also ensure that we follow forward compatibility design patterns outlined by Gallagher (e.g [HATEOAS](https://gallaghersecurity.github.io/cc-rest-docs/ref/events.html)) so you as a developer don't have to worry about it.

While it's optional to read this chapter if you are simply using the API client or the tools. If you choose to develop the client further then this is a must read.

## Data Transfer Objects

Data Transfer Objects (DTOs) are used to parse the JSON payloads exchanged with the Gallagher REST endpoints. This is to ensure strict validation of the payloads. At it's heart each one of these classes are a `pydatic` parser.

There are three types of schema definitions, each one of them suffixed with their intent:

- **Ref** are `References` to other objects, they using contain a `href` and possibly additional meta data such as a `name` or `id`
- **Summary** is what is returned by the Gallagher API in operations such as [searches](https://gallaghersecurity.github.io/cc-rest-docs/ref/cardholders.html), these are generally a subset of the full object
- **Detail** are the full object found at a particular `href`, they compound on the `Summary` schema and add additional attributes
- **Responses** are resposnes sent back from the server, these will typically contain a set of `Summary` or `Detail` objects. When fetching _detailed_ responses for an object the server will often respond with a `Detail` object without a wrapper `Response` object.

I additional we have classes that defined responses which are suffixed with **Response**, these wrap structures which returns `hrefs` for `next` and `previous` responses and usually have a collection to hold the response.

Ensure that each Endpoint defines their own DTOs so you can test them for authenticity. Avoid writing generic classes.

While `Refs`, `Summary` and `Detail` responses have fields, and it would make sense from an efficiency point of view to inherit e.g `Summary` builds on `Ref`, this should be avoided so logically an instance of a `Ref` class doesn't assert true for `isinstance` of a `Summary` class.

### Utilities

Mixins:

- `IdentityMixin` - provides an `id` field
- `HrefMixin` - provides an `href` field
- `OptionalHrefMixin` - provides an `href` field that is optional

Base models:

- `AppBaseModel` - `IdentityMixin` and `HrefMixin`
- `AppBaseResponseModel` - distinguishes between a model vs a response that encapsulates a objects
- `AppBaseResponseWithFollowModel` - a response model with follow paths

### Writing DTO classes

Write about using OptionalHrefMixin

Naming convensions of DTO classes.

Organising DTO classes, where do extension resources like `CardholderAccessGroupSummary` go?

### Python Reserved Words

`from_optional_datetime` and `until_optional_datetime`

`type` as a variable name is acceptable for now

## API Client Core

The `core` package in `cc` provides two important classes:

- `APIEndpoint` which all endpoint consumers configuration must inherit from
- `EndpointConfig` an instance of which each class must return as a result of the `get_config` method

Every Endpoint Consumer Class is expected to return an instance of `EndpointConfig` from the `get_config` method. Each configuration provides references to paths that are dynamically discovered as part of our bootstrapping process.

Never hard code URLs as this violates the [HATEOAS](https://en.wikipedia.org/wiki/HATEOAS) design principle.

Additionally each configuration will provide references to DTO classes that is used to parse responses, and details of the body.

```py
class Alarms(
    APIEndpoint
):
    """ Alarms
    """

    @classmethod
    async def get_config(cls) -> EndpointConfig:
        return EndpointConfig(
            endpoint=Capabilities.CURRENT.features.alarms.alarms,
            dto_list=AlarmSummaryResponse,
            dto_retrieve=AlarmSummary,
        )
```

The above example shows the `Alarms` class which is a consumer of the `alarms` endpoint. It nominates `AlarmSummaryResponse` as the class the infrastructure will use to parse `list` responses and `AlarmSummary` as the class to parse `retrieve` responses.

It references the `Capabilities.CURRENT` singleton which is a `Capabilities` instance that is bootstrapped at runtime. This is a singleton that is used to provide references to all endpoints.

If a command centre does not have a certain capability then the objects are set to `None` and accessing the feature raises an exception (more on this in other sections).

### Designing Endpoint Consumers

Each API consumer inherits from `APIEndpont` which is defined in `gallagher.cc.core`. Before each endpoint is executed we run an internal discovery process (see the `_discover` method in `APIEndoint` class).

We do this to be forwards compatible (see [HATEOAS chapter](https://gallaghersecurity.github.io/cc-rest-docs/ref/events.html) in Gallagher's documentation), but caches the response across a session (a session being an application life cycle) to increase API round trip performance.

The discovered state of the server is stored in a singleton, that's used by all the API endpoints. This can be found in the `core` package, as the `CURRENT` attribute of the `Capabilities` class. This is always an instance of `DiscoveryResponse`. Because this is instantiated as part of the bootstrap, initially all the URLs are set to `None`, the values are populated ahead of the first API call made to the server.

For this reason all `APIEndpoint` classes return a configuration as a result of a function called `get_config` (an `async` method that at a `class` scope) as opposed to a statically assigned class variable (otherwise the URLs would always result to be the initial `None` value).

!!! tip

    If you want to force discovery of the endpoints call `expire_discovery` on the `APIEndpoint` before calling the API endpoint. e.g `Cardholder.expire_discovery()`

```python
from ..core import (
    Capabilities,
    APIEndpoint,
    EndpointConfig
)

from ...dto.detail import (
    DivisionDetail,
)

from ...dto.response import (
    DivisionSummaryResponse,
)

class Division(APIEndpoint):
    """
    Gallagher advises against hard coding the URLs for divisions, and instead
    recommends using the /api endpoint to discover the URLs from
    events.divisions.href and alarms.division.href.

    """

    @classmethod
    async def get_config(cls) -> EndpointConfig:
        return EndpointConfig(
            endpoint=Capabilities.CURRENT.features.divisions.divisions,
            dto_list=DivisionSummaryResponse,
            dto_retrieve=DivisionDetail,
        )
```

## Extending DTOs for the CLI

```python
    @property
    def cli_header(self):
        return ["Id", "First name", "Last name", "Authorised"]

    def __rich_repr__(self):
        return [r.__rich_repr__() for r in self.results]

    def __str__(self):
        return f"{len(self.results)} cardholders"
```

```py
class CardholderSummaryResponse(
    AppBaseResponseModel,
):
    """Summary response for cardholder list and search

    /api/cardholders is generally the endpoint that responds
    to the query, it is dynamically configured from the discovery

    """

    results: list[CardholderSummary]

    @property
    def cli_header(self):
        return ["Id", "First name", "Last name", "Authorised"]

    def __rich_repr__(self):
        return [r.__rich_repr__() for r in self.results]

    def __str__(self):
        return f"{len(self.results)} cardholders"
```

## CLI

## TUI

## SQL
