# API Client Design

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

## API Client Core

The `core` package in `cc` provides two important classes:

- `APIEndpoint` which all endpoint consumers configuration must inherit from
- `EndpointConfig` an instance of which each class must return as a result of the `get_config` method

Every Endpoint Consumer Class is expected to return an instance of `EndpointConfig` from the `get_config` method. Each configuration provides references to paths that are dynamically discovered as part of our bootstrapping process.

Never hard code URLs as this violates the [HATEOAS](https://en.wikipedia.org/wiki/HATEOAS) design principle.

Additionally each configuration will provide references to DTO classes that is used to parse responses, and details of the body.

```
class Alarms(
    APIEndpoint
):
    """ Alarms
    """

    @classmethod
    async def get_config(cls) -> EndpointConfig:
        return EndpointConfig(
            endpoint=Capabilities.CURRENT.features.alarms.alarms,
            dto_list=AlarmResponse,
            dto_retrieve=AlarmZoneSummary,
        )
```

The above example shows the `Alarms` class which is a consumer of the `alarms` endpoint. It nominates `AlarmResponse` as the class the infrastructure will use to parse `list` responses and `AlarmZoneSummary` as the class to parse `retrieve` responses.

It references the `Capabilities.CURRENT` singleton which is a `Capabilities` instance that is bootstrapped at runtime. This is a singleton that is used to provide references to all endpoints.

If a command centre does not have a certain capability then the objects are set to `None` and accessing the feature raises an exception (more on this in other sections).

### Designing Endpoint Consumers

## Layout

Layout of our files

```
.
├── assets
├── docs
│   └── docs
├── gallagher
│   ├── cc
│   │   ├── alarms
│   │   ├── cardholders
│   │   └── status_overrides
│   ├── cli
│   ├── dto
│   │   ├── detail
│   │   ├── ref
│   │   ├── response
│   │   └── summary
│   └── tui
└── tests
```

## Toolchain

Majority of the development was conducted on macOS, but the toolchain should be compatible with any operating system. All elements of the project were developed in `python` with standard tooling

In addition we use:

- `task` - as the task runner of choice, it's widely avilable on platforms and supports Github actions. All endpoints are documented within the command line tool.
- `poetry` as our package manager of choice for the python project


