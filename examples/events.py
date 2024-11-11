""" Alarms

Demonstrations of various useful features around alarms, starting
with tailing the alarms log, and then moving on to acknowledging

"""
import os
import asyncio

from gallagher import cc
from gallagher.cc.alarms.events import Event
from gallagher.cc.cardholders import Cardholder

async def main():
    api_key = os.environ.get("GACC_API_KEY")
    cc.api_key = api_key

    event = asyncio.Event()
    event.set()

    async for updates in Event.follow(
        event=event,
    ):
        for update_event in updates.events:
            if update_event.cardholder:

                ch = await Cardholder.retrieve(update_event.cardholder.id)
                print(ch)
    

if __name__ == "__main__":
    asyncio.run(main())