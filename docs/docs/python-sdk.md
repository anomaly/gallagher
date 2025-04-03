# Python API Client

Gallagher Python Toolkit started life with the API Client, and it underpins all the utilities GPT ships. The central theme in the API client is data validation for responses and payloads. We take the approach of "nothing can go wrong" when we are interacting with a Gallagher Command Centre. We put in enormous effort into maintaining this SDK with the following aims:

- **Stellar DX** - We've put immense effort in designing the programming interface to provide a stellar developer experience. If you've worked with well designed API clients like Stripe, you should feel right at home.
- **Merciless validation** - built on top of [pydantic](https://pydantic.dev) the SDK ensures extremely strong data validation, reenforced with a complete set of tests.
- **Designed to Perform** - throughout the development we identified and fine tuned every portion to steal milliseconds back without compromising on the reliability.
- **Future proof** - HATEOAS support ensures that the SDK is future proof and designed to standards outlined by Gallagher.
- **Built for tomorrow** - `asyncio` support ensures that the SDK is ready for the upcoming future of Python.

## Setup

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

## Data Transfer Objects (DTO) premiere

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

## API endpoint lifecycle

You do not need to look under the hood to work with the API client. This section was written for you to understand how we implement Gallagher's requirements for standard based development. Each endpoint inherits from a base class called `APIEndpoint` defined in `gallagher/cc/core.py` and provides a configuration that describes the behaviour of the endpoint (in accordance with the Command Centre API).

Before your request is sent, the endpoint will:

- Run a method called `_discover` (this is only ever run once per session, i.e so long as the client instance is in memory), this discovers and caches API endpoints in accordance to the HATEOAS principle.
- The `get_config` method is executed to bootstrap the environment and using the above discovery results.
- Runs your request and returns the response where appropriate.

You can read about his in [our design document](design.md).

## Configuration

You are required to set the `api_key` once across your usage of the SDK. You can typically do this by import `cc` from the `gallagher` package and setting the `api_key` attribute.

```python
import os
from gallagher import cc

api_key = os.environ.get("GACC_API_KEY")
cc.api_key = api_key
```

You can obviously obtain the `api_key` from a secure location such as a secret manager or a configuration file.

!!! warning

    Never publish the API Key in your code or in a public repository. API keys have various
    levels of permission on your command centre and leaking the key can cause serious damage.

    If you think your API key has been compromised, please revoke it immediately.

By default the API client is configured to use the `Australian` cloud gateway to communicate with your Command Centre. You can override this to:

- FQDN of a different cloud gateway (currently supported are Australia and United States)
- IP address of a cloud gateway (current supported are Australia and United States)
- FQDN or IP address of a local Command Centre (not using a cloud gateway)

`gallagher.const` provides an easy way to reference these values and are maintained by the SDK. We recommend you rely on them, instead of hardcoding the values in your application.

If you wish to target a different cloud gateway, use the constants:

- `URL.CLOUD_GATEWAY_AU` - for the Australian cloud gateway
- `URL.CLOUD_GATEWAY_US` - for the United States cloud gateway

If you wish to target the cloud gateway via IP address, use the constants:

- `IP_ADDR.CLOUD_GATEWAY_AU` - for the Australian cloud gateway
- `IP_ADDR.CLOUD_GATEWAY_US` - for the United States cloud gateway

!!! note

    If you target the cloud gateway via IP addresses, Gallagher provides a set of addresses
    which are passed as an array to the `APIEndpoint` class. The SDK will automatically
    cycle through the addresses in case of a failure.

You can override the address of the gateway in a similar the way to setting the `api_key`:

```python
from gallagher import cc
from gallagher.const import URL

cc.api_base = URL.CLOUD_GATEWAY_US
```

In cases where you are targeting a local Command Centre, you can set the `api_base` to the FQDN or IP address of the Command Centre that's locally accessible on the network.

### Proxy support

Thanks to `httpx` we have proxy support built in out of the box. By default the `proxy` is set to `None` indicating that one isn't in use. If you wish to use a proxy for your use case, then simply set the `proxy` attribute on the `cc` object like you would the `api_base` or `api_key`.

```python
from gallagher import cc

cc.proxy = "http://username:password@proxy.example.com:8080"
```

For information on advanced configuration options [see the httpx documentation](https://www.python-httpx.org/advanced/proxies/). As always be very careful where you retrieve the proxy information from, and do not version control it.

## Usage

Once you have an environment up and running you can start using the SDK to interact with the Command Centre API. The following demonstrates a very basic example of fetching a list of cardholders.

If the command centre returns a result the SDK will parse the response and return a Python object which you can interact with or use for further queries.

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

!!! note

    We encourage the use of `asyncio` where possible. In case you are unable to use `asyncio`
    please refer to our advanced guide for strategies to work around this.

We provide a streamlined pattern of calls that the developers can use across data types to access the various Gallagher API Endpoints. For the purposes for this guide we will use the `Item` endpoint to elaborate how the SDK wraps the usual suspects and additional methods (where applicable to endpoints).

Each Endpoint has a configuration that determines which ones of the following methods are available. While our documentation outlines what is available, you will be met with an exception if you happen to call a method that isn't supported by the endpoint.

### Lists

The simplest interaction you can have with objects is to get a summary of objects. We refer to this operation as a `list` and they can be accessed by calling the `list` method on the appropriate endpoint. Each list method returns a `Response` object which contains a list of `Summary` or `Ref` objects.

These summary of ref objects are contained in a collection usually called `results` (this can vary per endpoint), the results are iterable, each item will be parsed object of the nominated model.

```python
from gallagher.dto.summary import (
    ItemSummary,
)

from gallagher.dto.response import (
    ItemTypesResponse,
    ItemsSummaryResponse,
)

from gallagher.cc.alarms.items import Item

# Get a list of items
response = await Item.list()

# Print the href to prove we have results
for item in response.results:
    print(item.href)
```

### Detail

You can fetch a detail of an object by calling the `retrieve` method on the appropriate endpoint. The `retrieve` method requires an `id` for the object and returns a `Detail` object which contains the full set of attributes for the object.

```python
from gallagher.dto.summary import (
    ItemSummary,
)

from gallagher.dto.response import (
    ItemTypesResponse,
    ItemsSummaryResponse,
)

from gallagher.cc.alarms.items import Item

# Get a list of items
detail_response = await Item.retrieve(399)
```

!!! note

    The `retrieve` method uses `id` instead of a reference to an object because it's a generic
    wrapper wants to construct the URL based on the parameter rather than the developer
    passing in a `href` which could result in the user passing in an `href` to a different object.

### Search

### Creating

### Deletion

### Additional Methods

Many of the endpoints provide additional mutations to interact with the Command Centre. The SDK makes sensible decisions to combine endpoints where it makes sense. For example, the `Alarm` endpoint provides an endpoint to mark an alarm as viewed, additionally with a comment.

```python
    @classmethod
    async def mark_as_viewed(
        cls,
        alarm: AlarmRef | AlarmSummary | AlarmDetail,
        comment: Optional[str],
    ) -> bool:
```

## Next and Updates

If an `APIEndpoint` claims that to supports pagination, it will automatically expose the following methods. Each one of these is designed to follow the path based on the responses from the Gallagher API. You are to rely on the `next`, or `previous` attribute to determine if there are more items to fetch.

- `next` - uses the `next` `href` to follow the next set of items
- `previous` - uses the `previous` `href` to follow the previous set of items

```python
items_summary = await Item.list()

# Iterate until the next attribute is None
while items_summary.next:
    # Will use the next href to fetch the next set of items
    items_summary = await Item.next(items_summary)
```

!!! note

    You don't provide a `url` or `href` to the `next` or `previous` methods, they are automatically
    determined from the response object. This ensures that we can update the SDK as the API changes
    leaving your code intact.

## Follow for changes

Entities like `Cardholders`, `Alarms`, `Items`, and `Event` provide `updates` or `changes`, that can be monitored for updates. Essentially these are long poll endpoints that:

- Provide a set of recent update as a `Summary` Response
- End with an `next` URL which provides the next set of updates
- Returns an empty set of updates if there are no updates within around 30 seconds
- Always returns a `next` URL to follow, even in the case of an empty set of updates

The SDK provide a clean `async` way of following these updates where you can run a `for` loop over an `async` generator which `yields` updates as they are available.

It uses an `asyncio` event to control the loop, and you can stop the loop by calling `event.clear()`. This is so you can control the event loop based on an application level trigger e.g a user navigating to a particular interface.

Here's a sample of how you can follow updates and stop the loop if there are no updates:

```python
import os
import asyncio

from gallagher import cc
from gallagher.cc.alarms import Alarms

async def main():
    api_key = os.environ.get("GACC_API_KEY")
    cc.api_key = api_key

    # Used to control the event loop
    asyncio_event = asyncio.Event()
    asyncio_event.set()

    async for updates in Alarms.follow(
        asyncio_event=asyncio_event,
    ):

        for update in updates.updates:
            print(update)

        # Examples of stopping the loop if
        # we got no updates
        if len(updates.updates) == 0:
            asyncio_event.clear()

if __name__ == "__main__":
    asyncio.run(main())
```

Endpoints that provide either an `update` or a `change` method will provide:

- `endpoint_follow` which will be the HATEOS discovered endpoint
- `dto_follow` which is a DTO class (typically a Summary) to be used to parse the updates

Following is an extract from the `Alarm` class to demonstrate how it's configured:

```python
@classmethod
async def get_config(cls) -> EndpointConfig:
    """Return the configuration for Alarms

    Arguments:
    cls: class reference
    """
    return EndpointConfig(
        endpoint=Capabilities.CURRENT.features.alarms.alarms,
        endpoint_follow=Capabilities.CURRENT.features.alarms.updates,
        dto_follow=AlarmUpdateResponse,
        dto_list=AlarmSummaryResponse,
        dto_retrieve=AlarmDetail,
    )
```

!!! warning

    As a breaking change in `8.90` the operator must have the 'Create Events and Alarms' privilege in the division of the source item, if your request specifies a source item. Current versions only require that the operator has that privilege on at least one division.

## Error Handling

### Exceptions

These wrappers raise the following `Exceptions` when they encounter the corresponding HTTP codes:

- `gallagher.exception.UnlicensedFeatureException` on `HTTPStatus.FORBIDDEN` when an unlicensed endpoint is accessed (see the discovery section for details)
- `gallagher.exception.AuthenticationError` on `HTTPStatus.UNAUTHORIZED` if there are issues with authentication
- gallagher.exception.NotFoundException`on`HTTPStatus.NOT_FOUND`(GET only) - raised if a HTTP endpoint wasn't found e.g A`Detail` object wasn't found

### Warnings

## Additional Features

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
