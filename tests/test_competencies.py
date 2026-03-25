""" Test Competency endpoints

"""

import pytest

from gallagher.cc import APIClient
from gallagher.dto.detail import CompetencyDetail
from gallagher.dto.response import CompetencyResponse
from gallagher.cc.competencies import Competency


@pytest.fixture
async def competency_summary(api_client: APIClient) -> CompetencyResponse:
    """Makes a single call to the competency list"""
    response = await api_client.competencies.list()
    return response


async def test_competency_list(competency_summary: CompetencyResponse):
    """Test listing competencies"""
    assert type(competency_summary) is CompetencyResponse
    assert type(competency_summary.results) is list
    assert len(competency_summary.results) > 0


async def test_competency_detail(
    api_client: APIClient,
    competency_summary: CompetencyResponse,
):
    """Test getting the details of a competency"""
    for c_summary in competency_summary.results:
        if not c_summary.id:
            pytest.skip(
                'Competency summary missing id, cannot retrieve detail.')
        c_detail = await api_client.competencies.retrieve(c_summary.id)
        assert type(c_detail) is CompetencyDetail
        assert c_detail.id == c_summary.id
