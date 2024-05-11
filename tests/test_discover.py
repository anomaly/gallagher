""" Discover the API.

"""

import pytest
import httpx

from gallagher import cc
from gallagher.cc import core

from gallagher.dto.detail import (
    FeaturesDetail,
)
from gallagher.dto.response import (
    DiscoveryResponse,
)


@pytest.fixture
async def discover_response() -> DiscoveryResponse:
    """Makes sure that the API is discoverable as per HATEOAS

    This is not an endpoint like the others, because it is a discovery
    protocol and must be run before any other items are executed.

    :return: DiscoveryResponse
    """

    async with httpx.AsyncClient() as _httpx_async:
        response = await _httpx_async.get(
            cc.api_base,
            headers=core._get_authorization_headers(),
        )

        await _httpx_async.aclose()

        parsed_obj = DiscoveryResponse.model_validate(response.json())

        return parsed_obj


async def test_discover_response(discover_response: DiscoveryResponse):
    """Process to see if the discovery method is legit"""
    assert type(discover_response) is DiscoveryResponse
    assert type(discover_response.features) is FeaturesDetail
    assert type(discover_response.version) is str
    assert len(discover_response.version) > 0
