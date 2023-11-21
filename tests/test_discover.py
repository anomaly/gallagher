""" Discover the API.

"""


def test_discover():

    from gallagher.cc import APIFeatureDiscovery
    from gallagher.dto.discover import (
        DiscoveryResponse,
        FeaturesDetail
    )

    response = APIFeatureDiscovery.list()
    assert type(response) is DiscoveryResponse
    assert type(response.features) is FeaturesDetail
