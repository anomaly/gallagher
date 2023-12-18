""" Alarms


"""

import os

from gallagher import cc
from .utils import AsyncTyper

api_key = os.environ.get("GACC_API_KEY")

cc.api_key = api_key

app = AsyncTyper()
