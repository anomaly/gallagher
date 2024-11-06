""" Alarms

Demonstrations of various useful features around alarms, starting
with tailing the alarms log, and then moving on to acknowledging

"""
import os
import asyncio

from gallagher import cc
from gallagher.cc.alarms.events import Event

async def main():
    api_key = os.environ.get("GACC_API_KEY")
    cc.api_key = api_key

    event = asyncio.Event()
    event.set()

    print("here")
    async for updates in Event.follow(
        event=event,
    ):
        
        print("here")
        for update in updates.updates:
            print(update)

        if len(updates.events) == 0:
            event.clear()

    

if __name__ == "__main__":
    asyncio.run(main())