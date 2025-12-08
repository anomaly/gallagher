""" Command Centre bindings

    After enabling the Gateway for your server and REST API user, you need 
    only to replace the local server's URL with the cloud API Gateway one.

    Example Local request:

        <client certificate thumbprint e89ef121958...>
        GET https://servername.yourcompany.local:8904/api/cardholders
        Authorization: GGL-API-KEY F6F0-C8F0-
        
    Equivalent Gateway request:

        <client certificate thumbprint e89ef121958...>
        GET https://commandcentre-api-au.security.gallagher.cloud/api/cardholders
        Authorization: GGL-API-KEY F6F0-C8F0-60AF-

    The API client takes of appending the headers onto the requests.

    The packages mimic the documentation structure presented by Gallagher on their
    Github pages https://gallaghersecurity.github.io/cc-rest-docs/ref/index.html
"""

from typing import Optional
from datetime import datetime

import httpx

from ..dto.detail.discover import (
    FeaturesDetail,
)
from ..dto.response import (
    DiscoveryResponse,
)

from .core import (
    CommandCentreConfig,
    RequestHeadersMixin,
)

from .access_groups import AccessGroup
from .alarms import Alarm
from .alarms.divisions import Division
from .alarms.day_category import DayCategory
from .alarms.events import Event, EventType, EventGroup
from .alarms.events import Event, EventType, EventGroup
from .alarms.items import ItemsType, Item
from .alarms.schedule import Schedule
from .cardholders import Cardholder, PdfDefinition
from .cardholders.card_type import CardType
from .doors import Door
from .lockers import Locker
from .operators import Operator
from .receptions import Reception
from .roles import Role
from .visitors import Visitor
from .visits import Visit
from .zones import Zone

class APIClient(RequestHeadersMixin,):
    """ Command Centre REST API client configuration holder """

    """ This configuration must be initialised ahead of time

    We pass this object around to the rest of the API clients for
    them to behave uniformly.
    """
    config: CommandCentreConfig

    """
    Discover response object, each endpoint will reference
    one of the instance variable Href property to get the
    path to the endpoint.

    Gallagher recommends that the endpoints not be hardcoded
    into the client and instead be discovered at runtime.

    Note that if a feature has not been licensed by a client
    then the path will be set to None, if the client attempts
    to access the endpoint then the library will throw an exception

    This value is memoized and should be performant
    """
    _CAPABILITIES: DiscoveryResponse


    access_groups: AccessGroup
    alarms: Alarm
    divisions: Division
    day_categories: DayCategory
    events: Event
    event_types: EventType
    event_groups: EventGroup
    items: Item
    item_types: ItemsType
    schedules: Schedule
    card_types: CardType
    cardholders: Cardholder
    pdf_definitions: PdfDefinition
    doors: Door
    lockers: Locker
    operators: Operator
    receptions: Reception
    roles: Role
    visitors: Visitor
    visits: Visit
    zones: Zone


    def __init__(self, config: Optional[CommandCentreConfig] = None):
        
        self.config = config or CommandCentreConfig()
        
        self._CAPABILITIES = DiscoveryResponse(
            version="0.0.0.0",  # Indicates that it's not been discovered
            features=FeaturesDetail(),
        )

        # Run the initially discovery to populate HATEOAS endpoints
        self.discover()

        # Initialise the rest of the API clients
        self.access_groups = AccessGroup(
            config=self.config,
            capabilities=self._CAPABILITIES
        )

        self.alarms = Alarm(
            config=self.config,
            capabilities=self._CAPABILITIES
        )

        self.divisions = Division(
            config=self.config,
            capabilities=self._CAPABILITIES
        )

        self.day_categories = DayCategory(
            config=self.config,
            capabilities=self._CAPABILITIES
        )

        self.events = Event(
            config=self.config,
            capabilities=self._CAPABILITIES
        )

        self.event_types = EventType(
            config=self.config,
            capabilities=self._CAPABILITIES
        )

        self.event_groups = EventGroup(
            config=self.config,
            capabilities=self._CAPABILITIES
        )

        self.items = Item(
            config=self.config,
            capabilities=self._CAPABILITIES
        )

        self.item_types = ItemsType(
            config=self.config,
            capabilities=self._CAPABILITIES
        )

        self.schedules = Schedule(
            config=self.config,
            capabilities=self._CAPABILITIES
        )

        self.card_types = CardType(
            config=self.config,
            capabilities=self._CAPABILITIES
        )

        self.cardholders = Cardholder(
            config=self.config,
            capabilities=self._CAPABILITIES
        )

        self.pdf_definitions = PdfDefinition(
            config=self.config,
            capabilities=self._CAPABILITIES
        )

        self.doors = Door(
            config=self.config,
            capabilities=self._CAPABILITIES
        )

        self.lockers = Locker(
            config=self.config,
            capabilities=self._CAPABILITIES
        )

        self.operators = Operator(
            config=self.config,
            capabilities=self._CAPABILITIES
        )

        self.receptions = Reception(
            config=self.config,
            capabilities=self._CAPABILITIES
        )

        self.roles = Role(
            config=self.config,
            capabilities=self._CAPABILITIES
        )

        self.visitors = Visitor(
            config=self.config,
            capabilities=self._CAPABILITIES
        )

        self.visits = Visit(
            config=self.config,
            capabilities=self._CAPABILITIES
        )

        self.zones = Zone(
            config=self.config,
            capabilities=self._CAPABILITIES
        )

    def discover(self):
        """The Command Centre root API endpoint

        Much of Gallagher's API documentation suggests that we don't
        hard code the URL, but instead use the discovery endpoint by
        calling the root endpoint.

        This should be a singleton which is instantiated upon initialisation
        and then used across the other endpoints.

        For example features.events.events.href is the endpoint for the events
        where as features.events.events.updates is the endpoint for getting
        updates to the changes to events.

        This differs per endpoint that we work with.

        Note that references to self._CAPABILITIES as a singleton, while
        cls.method when executing a class method.

        :params class cls: The class that is calling the method
        """

        if not self._CAPABILITIES.version == "0.0.0.0" and isinstance(
            self._CAPABILITIES._good_known_since, datetime
        ):
            # We've already discovered the endpoints as per HATEOAS
            # design requirement, however because the endpoint configuration is
            # dynamically populated, we have to call the get_config method
            return

        with httpx.Client(
            proxy=self.config.proxy,
            verify=self.config.ssl_context,
        ) as _httpx_async:
            # Don't use the _get wrapper here, we need to get the raw response
            response = _httpx_async.get(
                f"{self.config.api_base}",
                headers=self._get_authorization_headers(),
            )

            parsed_obj = DiscoveryResponse.model_validate(
                response.json()
            )

            # Assign the capabilities to the class, this should
            # result in the endpoint
            #
            # With the refactored initialisation of the pydantic
            # models, the values for the unavailable endpoints
            # should be set to None
            self._CAPABILITIES = parsed_obj

    def expire_discovery(self):
        """Expires endpoint discovery information

        Use this with caution as it significantly increases roundtrip times
        and decreases API client performance.

        Unless the server instance updates mid cycle, there should be no
        reason for these discovered URLs to change.
        """
        self._CAPABILITIES = DiscoveryResponse(
            version="0.0.0.0",  # Indicates that it's not been discovered
            features=FeaturesDetail(),
        )
