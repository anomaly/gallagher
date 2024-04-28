# API Client Design

A central feature to this client is it's detailed design, focused on a superior developer experience and performance. We also ensure that we follow design patterns outlined by Gallagher

## Data Transfer Objects

This a central part of our design. There are three types of schema definitions, each one of them suffixed with their intent:

- **Ref** are `References` to other objects, they using contain a `href` and possibly additional meta data such as a `name` or `id`
- **Summary** is what is returned by the Gallagher API in operations such as [searches](https://gallaghersecurity.github.io/cc-rest-docs/ref/cardholders.html), these are generally a subset of the full object
- **Detail** are the full object found at a particular `href`, they compound on the `Summary` schema and add additional attributes

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

### Designing Endpoints

## Layout

Layout of our files
