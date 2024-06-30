# Python API Client

Gallagher Python Toolkit started life with the API Client, and it underpins all the utilities GPT ships. The central theme in the API client is data validation for responses and payloads. We take the approach of "nothing can go wrong" when we are interacting with a Gallagher Command Centre. We put in enormous effort into maintaining this SDK with the following aims:

- A stellar developer experience for everyone building applications
- Reliability and the ability to constantly test changes against a real Command Centre
- Backwards compatibility to ensure your application don't break with our changes

Our aims is for you to write Python and we worry about how to best work with the Command Centre API.

# Setup

For most use cases we recommend installing a stable version from `pypi`.

Install via `pip` as follows:

```bash
pip install gallagher
```

or if you are using `poetry`:

```bash
poetry add gallagher
```

For production application please make sure you target a particular version of the API client to avoid breaking changes.

# Features

- **Stellar DX** - We've put immense effort in designing the programming interface to provide a stellar developer experience. If you've worked with well designed API clients like Stripe, you should feel right at home.
- **Merciless validation** - built on top of [pydantic](https://pydantic.dev) the SDK ensures extremely strong data validation, reenforced with a complete set of tests.
- **Designed to Perform** - throughout the development we identified and fine tuned every portion to steal milliseconds back without compromising on the reliability.
- **Future proof** - HATEOAS support ensures that the SDK is future proof and designed to standards outlined by Gallagher.
- **Built for tomorrow** - `asyncio` support ensures that the SDK is ready for the upcoming future of Python.

# Data Transfer Objects (DTO) Premiere

The Data Transfer Objects or DTOs are the centre piece of the Python SDK. These are built using the much loved [pyndatic](https://pydantic.dev) library. The aim is strict validation of responses and request payloads to ensure that the SDK never falls out of line with Gallagher' REST API.

Before every pull request is merged into our main branch, we run a full test suite against a demo Command Centre. See the [actions](https://github.com/anomaly/gallagher/actions) tab for a status of the latest build.

DTOs are classified into:

- `Refs` are the minimal pathway to an object
- `Summary` builds on a `Ref` and provides a subset of the attributes
- `Detail` builds on a `Summary` and provides the full set of attributes

A DTO is a subclass of one and only one of the above base classes. They deliberately do not inherit from each other so you can test of truths i.e a `ref` will never equate to a `summary` or a `detail`.

In addition to DTOs, you will see a number of :

- `Response` objects, which encapsulates a collection of `Summary` objects, they typically have `next` and `previous` paths for pagination
- `Payload` are the objects that are sent to the Command Centre to create or update an object

If you are fetching a `detail` then they are returned on their own as part of the response. They typically contain `href` to related objects.

# API Endpoint Lifecycle

Each endpoint inherits from a base class called `APIEndpoint` defined in `gallagher/cc/core.py`, it wrraps

`_discover`

`get_config`

# Basic Usage

We encourage the use of `asyncio` where possible.

```python title="Basic Usage"
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

## Lists

## Detail

## Search

## Creating

## Deletion

# Next and Updates

`next`

`previous`

# Error Handling

## Exceptions

## Warnings

# Additional Features

In addition to a nicely validated wrapper around the data sent by the Command Centre API, we provide provide the following helper interface to keep your interaction `pythonic` wherever possible.

## Personal Data Definitions

Personal Data Definitions are fields associated to a cardholder and are defined at a Command Centre level. These are dynamically discovered by calling the `/api/personal_data_fields`. When you fetch a cardholder detail, the API returns the `personal_data_fields` as part of the response in the following manner:

- children of the `personalDataFields` key in the cardholder detail
- accessible via key name prefixed with the `@` symbol i.e the personal data field `Email` is accessible via the key `@Email`

!!! tip

    Note that the `personDataFields` has a `list` of objects, and each object has a single key which is the nae of the personal data field and the value is the related data.

To make things more `pythonic` i.e consider the following payload (partially represented):

```json
{
  "@Cardholder UID": "2",
  "@City": "Hamilton",
  "@Company Name": "Gallagher Group",
  "@Country": "New Zealand",
  "@Email": "emma.bennett@gallagher.co",
  "@Personal URL": "C:\\DemoFiles\\CardholderURLs\\Emma Bennet.htm",
  "@Phone": "+64 7 838 9800",
  "@Photo": {
    "href": "https://commandcentre-api-au.security.gallagher.cloud/api/cardholders/340/personal_data/6550"
  },
  "firstName": "Emma",
  "href": "https://commandcentre-api-au.security.gallagher.cloud/api/cardholders/340",
  "id": "340",
  "lastName": "Bennett",
  "lastSuccessfulAccessTime": "2014-10-16T02:56:43Z"
}
```

and we had used the API client to fetch the cardholder detail (partial example):

```python title="Personal Data Fields"
cardholder = await Cardholder.retrieve(340)
```

you could access the `Email` field either via iterating over `cardholder.personal_data_definitions` and looking to match the `key` attribute of the object to `@Email` or using the parsed shortcut `cardholder.pdf.email`.

The above is achieved by dynamically populating a placeholder object with dynamically generated keys. These are parsed and populate _once_ when the object has successfully parsed the `JSON` payload.

!!! tip

    See pyndatic's [Model validator](https://docs.pydantic.dev/latest/concepts/validators/#model-validators) feature in v2, in particular the `@model_validator(mode='after')` constructor.
