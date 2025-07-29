import flet as ft
from config import settings
from controllers import home_controller

def main(page: ft.Page):
    settings.init(page)
    home_controller.init_game(page)

if __name__ == "__main__":
    ft.app(target=main)