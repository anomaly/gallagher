""" Events

"""
import os
import asyncio

from brother_ql import BrotherQLRaster, create_label
from brother_ql.backends.helpers import send
from PIL import Image, ImageDraw, ImageFont

from gallagher import cc
from gallagher.cc.alarms.events import Event
from gallagher.cc.cardholders import Cardholder

# Printer model and label size setup
PRINTER_MODEL = 'QL-700'  # Adjust to your printer model
LABEL_WIDTH = 696  # Common width in pixels for 62mm labels
LABEL_HEIGHT = 200  # Adjust for the height of your label

def create_basic_label(text):

    # Create a blank image with the specified background color
    image = Image.new('RGB', (LABEL_WIDTH, LABEL_HEIGHT), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    # Define the text and font
    font_size = 70
    font_color = (0, 0, 0)  # Black

    font = ImageFont.load_default(font_size)

    # Calculate the size of the text
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]

    # Calculate position for centered text
    text_x = (LABEL_WIDTH - text_width) // 2
    text_y = (LABEL_HEIGHT - text_height) // 2

    # Draw text on the image
    draw.text((text_x, text_y), text, fill=font_color, font=font)
    return image

async def main():
    api_key = os.environ.get("GACC_API_KEY")
    cc.api_key = api_key

    event = asyncio.Event()

    async for updates in Event.follow(
        asyncio_event=event,
    ):
        for update_event in updates.events:
            print("Processing event")
            if update_event.cardholder:
                print("Found cardholder in event")
                ch = await Cardholder.retrieve(update_event.cardholder.id)
                qlr = BrotherQLRaster(PRINTER_MODEL)
                # qlr.exception_on_warning = True  # Enable warnings if needed

                # Create label image and render to raster data
                label_image = create_basic_label(f"{ch.last_name}, {ch.first_name}")
                create_label(qlr, label_image, "62")

                # Define backend and specify the printer connection
                backend = 'pyusb'  # 'pyusb' for USB, 'network' if using network
                printer_identifier = 'usb://0x04f9:0x2042'  # Replace with actual printer USB ID or network IP
                print("Printing label")
                # Send the print job
                send(instructions=qlr.data, printer_identifier=printer_identifier, backend_identifier=backend)
    

if __name__ == "__main__":
    asyncio.run(main())