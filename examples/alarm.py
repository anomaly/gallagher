""" Alarms

Demonstrations of various useful features around alarms, starting
with tailing the alarms log, and then moving on to acknowledging

"""
import os
import asyncio

from gallagher import cc
from gallagher.cc.alarms import Alarms

async def main():
    api_key = os.environ.get("GACC_API_KEY")
    cc.api_key = api_key

    event = asyncio.Event()

    async for updates in Alarms.follow(
        asyncio_event=event,
    ):
        
        for update in updates.updates:
            print(update)

        if len(updates.updates) == 0:
            event.set()

    

if __name__ == "__main__":
    asyncio.run(main())