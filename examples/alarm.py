""" Alarms

Demonstrations of various useful features around alarms, starting
with tailing the alarms log, and then moving on to acknowledging

"""
import os
import asyncio

from gallagher import cc
from gallagher.cc.alarms import Alarms
from gallagher.dto.response import AlarmUpdateResponse

async def main():
    api_key = os.environ.get("GACC_API_KEY")
    cc.api_key = api_key

    event = asyncio.Event()
    event.set()

    async for updates in Alarms._follow(
        'https://commandcentre-api-au.security.gallagher.cloud/api/alarms/updates',
        AlarmUpdateResponse,
        event=event,
    ):
        print(f"Found update {len(updates.updates)}")

        if len(updates.updates) == 0:
            event.clear()

    

if __name__ == "__main__":
    asyncio.run(main())