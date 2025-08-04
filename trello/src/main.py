import flet as ft
from components.layout.navbar import Navbar
from components.layout.layout import Layout

def main(page: ft.Page):
    # settings
    page.title = "Flet Trello clone"
    page.padding = 0
    page.bgcolor = ft.Colors.BLUE_GREY_500
    page.theme = ft.Theme(font_family="Verdana")
    page.theme_mode = ft.ThemeMode.LIGHT
    page.theme.page_transitions.windows = ft.PageTransitionTheme.CUPERTINO
    page.fonts = {"Pacifico": "./fonts/Pacifico-Regular.ttf"}

    navbar = Navbar(page)
    layout = Layout(navbar, page)
    container = ft.Container(
        content=layout,
        expand=True,
        alignment=ft.alignment.top_center,
        padding=ft.padding.all(20),
    )
    page.add(container)
    page.update()


if __name__ == "__main__":
    ft.app(target=main, assets_dir="./assets")