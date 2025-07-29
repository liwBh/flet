import flet as ft

app_color = {
    "danger": "0xFF0000",
    "primary": "0x344AB3",
    "secondary": "0x949494",
    "success": "0x468A37",
    "warning": "0xFFFF00",
    "info": "0x00FFFF",
    "black": "0x000000",
    "white": "0xFFFFFF",
}

app_size = {
    "width": 450,
    "height": 800
}

app_font = {
}

def init(page):
    page.title = "Hangman"
    page.fonts = app_font
    page.theme = ft.Theme(font_family="zpix")
    page.window.width = app_size["width"]
    page.window.height = app_size["height"]
    page.window.resizable = False
    page.padding = 0
    page.update()
