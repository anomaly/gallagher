# SQL Interface

A central goal of the Python tools for Gallagher is assist enterprise to integrate corporate systems with the command centre. Use cases would involve systems like payroll, human resources applications that would want to toggle access or additionally keep abreast of events that have taken place in the command centre inline situ.

## Why SQL?

Copied verbatam from [shillelagh](https://github.com/betodealmeida/shillelagh?tab=readme-ov-file#why-sql) repository

> Sharks have been around for a long time. They're older than trees and the rings of Saturn, actually! The reason they haven't changed that much in hundreds of millions of years is because they're really good at what they do.
>
> SQL has been around for some 50 years for the same reason: it's really good at what it does.

[How to pronounce `shillelagh`](https://youtu.be/QHDZtvfTkz4?feature=shared) Shea-lay-lee

### ORM integration

## Adapter Design

`shillelagh` has appropriate documentation to [build your own adapters](https://shillelagh.readthedocs.io/en/latest/development.html#), the examples on the page go from implementing a simple adapter for the Weather API through to some tips to implement a more complex adapter that reads from an API e.g Google Sheets. It's recommended to study the source code to understand patterns of the how to provide data for more complex implementations.

Few things to address design wise are:

- Methods that allows shillelagh to [calculate the cost of a query](https://shillelagh.readthedocs.io/en/latest/development.html#estimating-query-cost)
- Strategies in mapping URLs to virtual tables
- How to dynamically provide a list of columns and results based on the table

> I spend some significant time in debugging registering my adapter and [wrote some notes to that effect](https://github.com/anomaly/gallagher/issues/31#issuecomment-2111223261), they are mostly around my strategy of how I got things going and using the `logger` to debug issues when using the interactive console.

The project features an extensive set of data transfer objects, strong design patterns and test suites to ensure that the interactions with the API are reliable.

The DTOs in particular capture the rules set out by the API documentation, primarily designed to enhance the developer experience.

It would thus make sense to extend the `EndpointConfig` class to include SQL specific configuration and the framework to inject the required configuration into the adapter.

The reason for extending `EndpointConfig` is to ensure that all related configuration is maintained in the base classes. The `adapter` amongst other things is an optional extension that:

- depends on the base API client to exist and function in full
- is optionally installed by the user

### Table names

The URL of th endpoint maps as the table name e.g:

```sql
🍀> SELECT * FROM "https://commandcentre-api-au.security.gallagher.cloud/api/cardholders";
```

where `https://commandcentre-api-au.security.gallagher.cloud/api/cardholders` is the table. The `adapter` would have acknowledged that it can handle this endpoint. If we support more than one than one endpoint then we would have to validate that the URL is one of the many.

### Field list

Each DTO is already aware of the fields and their types. If a type is a primitive then it's easy enough to handle.

If a field happens to be a relationship then we would have to return the ID of the object (if this is supported, not sure what to do when all it has is a href) to make it behave more SQL like. I think the child object should determine which field should be returned as the ID and the configuration should be part of the child object.

`SELECT` queries often let you specify while columns you wish to return. This also happens to be the case for the Gallagher API. See [#36](https://github.com/anomaly/gallagher/issues/36) for more information. It would make sense to combine these two patterns.

> Shillelagh require us to send back a field called `rowid` which has a unique identifier, we are currently using the `id` of the object as the `rowid`.

For partial queries we should take advantage of the fact that the CC API allows us to send a list of fields to return. This is a good way to reduce the amount of data that is returned.

### Search fields

Search fields are determined by the API per endpoint. These should be defined as `tuples` in the `EndpointConfig` class (note that tuples are immutable hence it's ideal for a configuration).

### Result Order

At this stage we support the defaults as defined by Shillelagh and allow the user to order results by any of the fields in the DTO.

The CC API does provide a `sort` query parameter that can be used to sort the results. Where possible we should use this parameter to avoid local computation costs. Note also the use of `-id` the negative sign to sort in descending order.

### Offset and Limit

The Gallagher API certain supports pagination, it does return a `next` link, and we might have to filter the results locally on the adapter. We should also cross reference our ticket on performance tuning [#14](https://github.com/anomaly/gallagher/issues/14)

### Query costing

Shillelagh has a method to calculate the cost of a query.

### Mapping pyndatic attributes to shillelagh

Our pyndatic classes use python typing to annotate fields for parsing. Shillelagh provides the `fields` package that allows developers of adapters to provide definition of fields handled by each virtual table.

To make this manageable for developers we need to provide a way to:

- register which endpoints are suited to work with our shillelagh adapters
- automatically map the fields from the pyndatic classes to the shillelagh fields

## Proposed API syntax

```python
    dto_list: Optional[any] = None  # DTO to be used for list requests
    dto_retrieve: Optional[any] = None  # DTO to be used for retrieve requests
```

`dto_list` object field should be used to determine fields that are returned when a list of objects is requested. The `dto_retrieve` object field should be used to determine fields that are returned when a single object is requested.

```python
    search_fields: Optional[Tuple[str]] = None  # Fields that can be searched
```

```python
    sql = False  # If the endpoint supports SQL queries
    sql_limit_supported = False  # If the endpoint supports SQL LIMIT
    sql_offset_supported = False # If the endpoint supports SQL OFFSET
```

SQL parsing things to check:

- The fields in a select exists in the DTO class
- Does an endpoint support offsets and limits
- Examples of joins, group by, order by, where clauses

Each top level package in gallagher.cc will defined a `tuple` called `__shillelagh__` this deliberately mounts classes that are to be used by the shillelagh adapter.

The framework calls the `get_columns` method which is to return a `Dict [str, Field]` where the key is the name of the field and the value is an instance of a `Field` class.

It's advisable to instantiate a list of columns in `init` and not compute them in the `get_columns` method.

### Mutations

Not all endpoints support mutations. The configuration of each DTO endpoint should reflect this. Our adapter will have to reflect this and proxy the operation to the DTO endpoint.

## Static references to Classes

I've decided to ad static references to the classes that support SQL to avoid using introspection.

## SQLAlchemy `dialect` Design

SQLAlchemy is a popular ORM (one of choice at Anomaly) and is supported by shillelagh. The `dialect` essentially makes available the endpoint as a virtual table to the ORM.
