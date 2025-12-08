""" Alarms

Command Centre raised alarms for 

"""

from typing import Optional

from ..core import (
    APIEndpoint,
    EndpointConfig,
)

from ...dto.ref import AlarmRef
from ...dto.summary import AlarmSummary
from ...dto.detail import AlarmDetail
from ...dto.response import (
    AlarmSummaryResponse,
    AlarmUpdateResponse,
)
from ...dto.payload import AlarmCommentPayload

class Alarms(
    APIEndpoint,
):
    """Alarms

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

    def get_config(self) -> EndpointConfig:
        """Return the configuration for Alarms

        Arguments:
        cls: class reference
        """
        return EndpointConfig(
            endpoint=self._CAPABILITIES.features.alarms.alarms,
            endpoint_follow=self._CAPABILITIES.features.alarms.updates,
            dto_follow=AlarmUpdateResponse,
            dto_list=AlarmSummaryResponse,
            dto_retrieve=AlarmDetail,
        )

    async def mark_as_viewed(
        self,
        alarm: AlarmRef | AlarmSummary | AlarmDetail,
        comment: Optional[str],
    ) -> bool:
        """ Mark an alarm as viewed

        arguments:
        alarm: AlarmRef | AlarmSummary | AlarmDetail
            The alarm to mark as viewed
        comment: Optional[str]
            A comment to add to the alarm 
        """
        await self._post(
            alarm.view.href,
            AlarmCommentPayload(comment=comment) if comment else None,
        )

        return alarm.href is not None

    async def comment(
        self,
        alarm: AlarmRef | AlarmSummary | AlarmDetail,
        comment: str,
    ) -> bool:
        """Comment on an alarm without changing status

        This will add a comment to the history of the alarm without
        changing the status of the alarm.

        You must pass a Ref, Summary or Detail which will be used
        to get the href of the Alarm

        arguments:
        alarm: AlarmRef | AlarmSummary | AlarmDetail
            The alarm to comment on
        comment: str
            The comment to add to the alarm
        """

        await self._post(
            alarm.comment.href,
            AlarmCommentPayload(comment=comment),
        )

        return alarm.href is not None

    async def mark_as_acknowledged(
        self,
        alarm: AlarmRef | AlarmSummary | AlarmDetail,
        comment: Optional[str],
    ) -> bool:
        """ Mark an alarm as acknowledged

        arguments:
        alarm: AlarmRef | AlarmSummary | AlarmDetail
            The alarm to mark as acknowledged
        comment: Optional[str]
            A comment to add to the alarm
        """
        await self._post(
            alarm.acknowledge.href,
            AlarmCommentPayload(comment=comment) if comment else None,
        )

        return alarm.href is not None

    async def mark_as_processed(
        self,
        alarm: AlarmRef | AlarmSummary | AlarmDetail,
        comment: Optional[str],
    ) -> bool:
        """ Mark an alarm as processed

        arguments:
        alarm: AlarmRef | AlarmSummary | AlarmDetail
            The alarm to mark as processed
        comment: Optional[str]
            A comment to add to the alarm 
        """
        await self._post(
            alarm.process.href,
            AlarmCommentPayload(comment=comment) if comment else None,
        )

        return alarm.href is not None

    async def mark_as_force_processed(
        self,
        alarm: AlarmRef | AlarmSummary | AlarmDetail,
    ) -> bool:
        """ Mark an alarm as force processed

        arguments:
        alarm: AlarmRef | AlarmSummary | AlarmDetail
            The alarm to mark as force processed

        returns:
        bool: True if the alarm was force processed 
        """
        await self._post(
            alarm.force_process.href,
            None,
        )

        return alarm.href is not None


# Write up Alarms for querying via the SQL interface
__shillelagh__ = (
    Alarms,
)