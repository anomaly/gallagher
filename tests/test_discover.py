""" Discover the API.

"""


def test_discover():

    from gallagher.cc import APIDiscovery
    from gallagher.dto.discover import (
        DiscoveryResponse,
        FeaturesDetail
    )

    response = APIDiscovery.list()
    assert type(response) is DiscoveryResponse
    assert type(response.features) is FeaturesDetail
