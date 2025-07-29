import flet as ft

app_color = {
    "primary": "0xFF0000",
    "black": "0x000000",
    "white": "0xFFFFFF",
    "blue": "0x344AB3",
    "blue_light": "0x00FFFF",
    "yellow": "0xFFFF00",
    "green": "0x468A37",
    "red": "0xED654A",
}

app_size = {
    "width": 450,
    "height": 800
}

app_font = {
    "zpix": "https://github.com/SolidZORO/zpix-pixel-font/releases/download/v3.1.9/zpix.ttf"
}

class AppState:
    current_pokemon = 0
    image = f"https://raw.githubusercontent.com/PokeAPI/sprites/4bcd17051efacd74966305ac87a0330b6131259a/sprites/pokemon/poke_id.png"

    @staticmethod
    def get_image():
        return AppState.image.replace("poke_id", str(AppState.current_pokemon))


def init(page):
    page.title = "Pokédex"
    page.fonts = app_font
    page.theme = ft.Theme(font_family="zpix")
    page.window.width = app_size["width"]
    page.window.height = app_size["height"]
    page.window.resizable = False
    page.padding = 0
    page.update()
