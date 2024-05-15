# SQL Interface

A central goal of the Python tools for Gallagher is assist enterprise to integrate corporate systems with the command centre. Use cases would involve systems like payroll, human resources applications that would want to toggle access or additionally keep abreast of events that have taken place in the command centre inline situ.

## Why SQL?

Copied verbatam from [shillelagh](https://github.com/betodealmeida/shillelagh?tab=readme-ov-file#why-sql) repository

> Sharks have been around for a long time. They're older than trees and the rings of Saturn, actually! The reason they haven't changed that much in hundreds of millions of years is because they're really good at what they do.
>
> SQL has been around for some 50 years for the same reason: it's really good at what it does.

[How to pronounce `shillelagh`](https://youtu.be/QHDZtvfTkz4?feature=shared) Shea-lay-lee

## Adapter Design

`shillelagh` has appropriate documentation to [build your own adapters](https://shillelagh.readthedocs.io/en/latest/development.html#), the examples on the page go from implementing a simple adapter for the Weather API through to some tips to implement a more complex adapter that reads from an API e.g Google Sheets. It's recommended to study the source code to understand patterns of the how to provide data for more complex implementations.

Couple of things to get note are:

- Methods that allows shillelagh to [calculate the cost of a query](https://shillelagh.readthedocs.io/en/latest/development.html#estimating-query-cost)
- Strategies in mapping URLs to virtual tables
- How to dynamically provide a list of columns and results based on the table

> I spend some significant time in debugging registering my adapter and [wrote some notes to that effect](https://github.com/anomaly/gallagher/issues/31#issuecomment-2111223261), they are mostly around my strategy of how I got things going and using the `logger` to debug issues when using the interactive console.

The project features an extensive set of data transfer objects, strong design patterns and test suites to ensure that the interactions with the API are reliable.

The DTOs in particular capture the rules set out by the API documentation, primarily designed to enhance the developer experience.

It would thus make sense to extend the `EndpointConfig` class to include SQL specific configuration and the framework to inject the required configuration into the adapter.

**Table names**: The URL of th endpoint maps as the table name e.g:

```sql
🍀> SELECT * FROM "https://commandcentre-api-au.security.gallagher.cloud/api/cardholders";
```

where `https://commandcentre-api-au.security.gallagher.cloud/api/cardholders` is the table. The `adapter` would have acknowledged that it can handle this endpoint. If we support more than one than one endpoint then we would have to validate that the URL is one of the many.

**Field list**

Each DTO is already aware of the fields and their types. If a type is a primitive then it's easy enough to handle.

If a field happens to be a relationship then we would have to return the ID of the object (if this is supported, not sure what to do when all it has is a href) to make it behave more SQL like. I think the child object should determine which field should be returned as the ID and the configuration should be part of the child object.

`SELECT` queries often let you specify while columns you wish to return. This also happens to be the case for the Gallagher API. See [#36](https://github.com/anomaly/gallagher/issues/36) for more information. It would make sense to combine these two patterns.

**Search fields**

Search fields are determined by the API per endpoint. These should be defined as `tuples` in the `EndpointConfig` class (note that tuples are immutable hence it's ideal for a configuration).

**Result Order**

**Offset and Limit**

The Gallagher API certain supports pagination, it does return a `next` link, and we might have to filter the results locally on the adapter. We should also cross reference our ticket on performance tuning [#14](https://github.com/anomaly/gallagher/issues/14)

## SQLAlchemy `dialect` Design
