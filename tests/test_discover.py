""" Discover the API.

"""

import ssl
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

    ssl_context = None

    if cc.file_tls_certificate and cc.file_private_key:
        ssl_context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
        ssl_context.load_cert_chain(
            cc.file_tls_certificate,
            cc.file_private_key
        )

    async with httpx.AsyncClient(
        proxy=cc.proxy,
        verify=ssl_context,
    ) as _httpx_async:
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
    assert isinstance(discover_response.features,
                      type(discover_response.features))
    assert type(discover_response.version) is str
    assert len(discover_response.version) > 0
