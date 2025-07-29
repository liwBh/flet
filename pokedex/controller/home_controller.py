import aiohttp
import asyncio
from config.configPage import AppState, app_color

async def get_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

def create_data_text(data):
    if not data:
        return ""

    abilities = ", ".join([ability["ability"]["name"] for ability in data["abilities"]])
    return f"Name: {data['name']}\nAbilities: {abilities}\nHeight: {data['height']} cm"


def update_screen(page, text, result, image):
    text.value = create_data_text(result)
    image.src = AppState.get_image()
    page.update()

async def blink(page, led):
    while True:
        await asyncio.sleep(1)
        led.bgcolor = app_color["blue_light"]
        page.update()
        await asyncio.sleep(0.5)
        led.bgcolor = app_color["blue"]
        page.update()


async def event_change(e, action, page, text, image, led):

    n = AppState.current_pokemon

    if action == "add":
        n = n + 1
        if n > 150:
            n = 150
    elif action == "subtract":
        n = n - 1
        if n < 1:
            n = 1

    AppState.current_pokemon = n

    result = await get_data( f"https://pokeapi.co/api/v2/pokemon/{n}")

    update_screen(page, text, result, image)

