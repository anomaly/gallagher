""" Discover the API.

"""

import pytest
import httpx

from gallagher.cc.core import (
    CommandCentreConfig,
    RequestHeadersMixin,
)

from gallagher.dto.response import (
    DiscoveryResponse,
)


@pytest.fixture
async def discover_response(cc_config: CommandCentreConfig) -> DiscoveryResponse:
    """Makes sure that the API is discoverable as per HATEOAS

    This is not an endpoint like the others, because it is a discovery
    protocol and must be run before any other items are executed.

    :return: DiscoveryResponse
    """

    header_mixin = RequestHeadersMixin()
    header_mixin.config = cc_config

    async with httpx.AsyncClient(
        proxy=cc_config.proxy,
        verify=cc_config.ssl_context,
    ) as _httpx_async:
        response = await _httpx_async.get(
            f"{cc_config.api_base}",
            headers=header_mixin._get_authorization_headers(),
        )

        await _httpx_async.aclose()

        parsed_obj = DiscoveryResponse.model_validate(response.json())

        return parsed_obj


async def test_discover_response(discover_response: DiscoveryResponse):
    """Process to see if the discovery method is legit"""
    assert type(discover_response) is DiscoveryResponse
    assert isinstance(discover_response.features,
                      type(discover_response.features))
    assert type(discover_response.version) is str
    assert len(discover_response.version) > 0
