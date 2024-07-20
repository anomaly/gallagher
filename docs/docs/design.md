# Contributor's Manual

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

The Developer Experience must be at the heart your thinking when you are extending the SDK, to assist with this the SDK provides the following utilities.

**Base models** - are classes that extend the `pyndatic` `BaseModel` class and provide common fields and configuration that are shared across all DTOs. Each DTO must inherit from one of the appropriate base models.

- `AppBaseModel` - is what a `Ref`, `Summary` or `Detail` class would inherit from
- `AppBaseResponseModel` - distinguishes between a model vs a response. A response has results which would in turn be a list of `Ref` or `Summary` objects
- `AppBaseResponseWithFollowModel` - as response as model as the one before but with `next`, `previous`, or `update` links (depending on the use case)

**Mixins** - are Python classes that inject a particular behaviour into a DTO. They abstract concepts like `id`, `href` and `optional_href` (which is defined using an annotation).

- `IdentityMixin` - provides an `id` field
- `HrefMixin` - provides an `href` field
- `OptionalHrefMixin` - provides an `href` field that is optional

using these is as simple as inheriting from them in your DTO classes e.g:

```python
from gallagher.dto.mixins import (
    IdentityMixin,
    HrefMixin,
    AppBaseModel,
)

class CardholderSummary(
    AppBaseModel,
    IdentityMixin,
    HrefMixin,
):
    """Summary of a cardholder

    This is a summary of a cardholder, it is typically returned
    in a list of cardholders.

    It would have an id and href field because of the Mixin
    """

    first_name: str
    last_name: str
    authorised: bool
```

### Writing DTO classes

DTOs are essentially `pyndatic` data models with some design assumptions. Most of these are around helpers we provide along with naming and placement conventions:

- **Suffix names with utlity** - we debated this a lot before deciding that it was more utiliatarian to suffix the classes with their utility e.g `CardholderSummary`, `CardholderDetail`, `CardholderRef`, this voids the needs for formally importing the classes and then aliasing them.
- **Use Mixins** - to provide common fields across DTOs, this reduces code duplication and ensures consistency, so wherever possible use the provided Mixins.
- **Caution on using OptionalHrefMixin** - this Mixin was initially introduced to model the HATEOAS discovery pattern (which we call the Discovery pattern), while this proves useful in some other use cases, we advice caution in making a `href` optional as we prefer to have a strict schema.
- **Placement of DTOs** - In most cases your DTOs will be placed by function e.g `ref`, `summary`, `detail`, however in cases where a model is returned explicitly as part of say a Detail response, and expands attributes e.g `CardholderAccessGroupSummary` (which defines a card assigned to a Cardholder) then this should be placed in the same page as the `detail`. In the inline examples you will find this in `detail/cardholder.py`.

### Conflicts with Python Reserved Words

Gallagher's API uses certain `keys` e.g `from` in their `json` responses that are reserved words in Python. To handle this we use the `pydantic` `Field` class to alias these fields. These are defined as annotations that you should use across the DTOs. A sample definition looks like (found in `dto/utils.py`):

```python
from_optional_datetime = Annotated[
    Optional[datetime],
    Field(..., alias="from")
]
```

Our current aliases are:

- `from_optional_datetime` - which is to be used for the `from` date fields
- `until_optional_datetime` - which is to be used for the `until` date fields, while `until` is not a reserved word in Python, we've chosen to use this to be consistent with the `from` field

`type` is another `key` that that constant appears in the `JSON` payloads, while this is a reserved function name in Python, it does not conflict with the compiler when used as a variable name. For now we've chosen not to wrap this in an alias.

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

### Transport Wrappers

`APIEndpoint` has several helper methods that reduce code duplication and ensures that the HTTP call lifecycle is handled properly.

- `_get` - provides a wrapper for HTTP `GET` calls, this takes in a mandatory `url` and an optional `response_class` which must be a subclass of `AppBaseModel`, typically a `Detail` or a `Response` class
- `_post ` - provides a wrapper for HTTP `POST` calls, and like `_get` takes in a `url` and `response_class`. In addition you pass in `payload` which must also be a subclass of `AppBaseModel`.

These wrappers raise the following `Exceptions` when they encounter the corresponding HTTP codes:

- `gallagher.exception.UnlicensedFeatureException` on `HTTPStatus.FORBIDDEN` when an unlicensed endpoint is accessed (see the discovery section for details)
- `gallagher.exception.NotFoundException`on`HTTPStatus.NOT_FOUND`(GET only) - raised if a HTTP endpoint wasn't found e.g A`Detail` object wasn't found
- `gallagher.exception.ComingSoonException` - raised if a feature is marked as "coming soon" by Gallagher
- `gallagher.exception.DeadEndException` - raised if you try and follow a path i.e `next` or `previous` on an endpoint that supports it but no longer has a path forward or back.
- `gallagher.exception.AuthenticationError` on `HTTPStatus.UNAUTHORIZED` if there are issues with authentication
- `gallagher.exception.PathFollowNotSupportedError` - raised if you try and call `next` or `previous` on an endpoint that does not support path follow.

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

## CLI

[Typer](https://typer.tiangolo.com) enhances [click](https://click.palletsprojects.com/en/8.1.x/) by providing a mode `FastAPI` like developer experience (having been created by the developers of FastAPI). The design of our `cli` is highly inspired by tools like `git`, and follows the subcommand pattern.

While we pride ourselves in providing a complete set of CLI commands, this section outlines thoughts on the design of the command line interface for those working on extending it.

### Extending DTOs for the CLI

The CLI interrogates the DTOs to build it's output. It does this by calling a set of predefined methods. These methods appear on the `Response` that in turn interrogates the `Summary` or `Detail` objects. You must think of these methods as returning a representation of itself for the command line.

!!! tip

    You are not responsible for formatting the output, the CLI will do this for you. The DTO is solely responsible for returning the data.

    If you are extending the CLI then please read the design patterns for presenting output. Remember, Developer Experience and Consistency is key.

A `Response` class must provide a representation of results it holds. Note that not all responses from the Gallagher API return the same keys, so you will have to override the methods per `Response` class.

The `cli_header` returns an array of strings that the CLI will use as headers for the table:

```python
@property
def cli_header(self):
    return ["Id", "First name", "Last name", "Authorised"]
```

The length of this list must match the length of the `__rich_repr__` method.

Next the CLI depends on calling the `__rich__repr__` method which standard rich representation (Typer and our CLI depends on the `rich` library to produce output). In many cases this created by amalgamating the fields form the results:

```python
def __rich_repr__(self):
    return [r.__rich_repr__() for r in self.results]
```

Finally the CLI depends on the standard `__str__` function to present sumamries of the results. Be mindful of what you send back as a response from this.

```python
def __str__(self):
    return f"{len(self.results)} cardholders"
```

Putting all this together if you were to return a list of `Cardholders` as part of the `Summary` call, it looks somewhat like this:

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

## TUI

## SQL

## Maintainers Notes

This section primarily contains notes for the managers of the project, it covers topics like publication of releases.

Much of this is automated via Github actions, these actions depend on the following secrets that have been set at a project level (and can only be updated by the project owners):

- `PYPI_API_KEY` - the API key for PyPI that is used to publish the package
- `GACC_API_KEY` - the API key for the Gallagher Command Centre that is used to run tests against.

### Publishing a Release

The action `.github/workflows/publish-package.yml` is responsible for publishing a release. This is triggered by a tag being pushed to the repository. The tag must be in the format `vX.Y.Z` where `X`, `Y` and `Z` are integers.

The `release` action will run the set of tests, and if they pass, it will publish the package to PyPI.

> [!IMPORTANT]
> In most instances you should not have to publish a release by hand. If there is ever a need to do that, we recommend that appropriate notes be left against the release.

### Writing Release Notes
