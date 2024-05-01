""" Alarms

Command Centre raised alarms for 

"""
from typing import Optional

from ..core import (
    APIEndpoint,
    EndpointConfig,
    Capabilities
)

from ...dto.ref import (
    AlarmRef,
)

from ...dto.summary import (
    AlarmSummary,
)

from ...dto.detail import (
    AlarmDetail,
)

from ...dto.response import (
    AlarmSummaryResponse,
)


class Alarms(
    APIEndpoint,
):
    """ Alarms

    Provides a standard set of operations for Alarms and in addition
    allows you to follow resulting actions to act on Alarms.

    To each action you are required to pass in a Ref, Summary or Detail
    and it picks the appropriate href to follow through 

    Current supported actions:
    - follow: 
    - comment:
    - mark_as_viewed:
    - mark_as_acknowledged:
    - mark_as_processed:
    - mark_as_force_processed:
    """

    @classmethod
    async def get_config(cls) -> EndpointConfig:
        """ Return the configuration for Alarms

        Agruments:
        cls: class reference
        """
        return EndpointConfig(
            endpoint=Capabilities.CURRENT.features.alarms.alarms,
            dto_list=AlarmSummaryResponse,
            dto_retrieve=AlarmDetail,
        )


    @classmethod
    async def follow(
        cls,
        href: str
    ) -> bool:
        """
        """
        return False

    @classmethod
    async def mark_as_viewed(
        cls,
        alarm: [
            AlarmRef|
            AlarmSummary|
            AlarmDetail
        ],
    ):
        """
        """
        pass

    @classmethod
    async def comment(
        cls,
        alarm: [
            AlarmRef|
            AlarmSummary|
            AlarmDetail
        ],
        comment: str,
    ) -> bool:
        """ Comment on an alarm without changing status

        This will add a comment to the history of the alarm without
        changing the status of the alarm.

        You must pass a Ref, Summary or Detail which will be used
        to get the href of the Alarm
        """

        

        return alarm.href is not None


    @classmethod
    async def mark_as_acknowledged(
        cls,
        alarm: [
            AlarmRef|
            AlarmSummary|
            AlarmDetail
        ],
        comment: Optional[str],
    ) -> bool:
        """
        """
        return False


    @classmethod
    async def mark_as_processed(
        cls,
        alarm: [
            AlarmRef|
            AlarmSummary|
            AlarmDetail
        ],
        comment: Optional[str],
    ) -> bool:
        """
        """
        return len(comment)>0


    @classmethod
    async def mark_as_force_processed(
        cls,
        alarm: [
            AlarmRef|
            AlarmSummary|
            AlarmDetail
        ],
    ) -> bool:
        """
        """
        return False

