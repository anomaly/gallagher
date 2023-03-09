"""

"""


from .utils import AppBaseModel, HrefMixin

class AlarmZoneRef(
    AppBaseModel,
    HrefMixin
):
    """ AccessZone represents
    """
    name: str

class AlarmZoneSummary(
    AppBaseModel,
):
    """ #TODO: Revise this if it shows up in other places

    I have literally named this class to model the alarm_zones
    property in the access_group schema. I don't know if this
    is appropriate
    """
    alarm_zone: AlarmZoneRef