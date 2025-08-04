import flet as ft
from components.layout.navbar import Navbar
from components.layout.layout import Layout

def main(page: ft.Page):
    # settings
    page.title = "Template"
    page.padding = 0
    page.bgcolor = ft.Colors.BLUE_GREY_500
    page.theme = ft.Theme(font_family="Verdana")
    page.theme_mode = ft.ThemeMode.LIGHT
    page.theme.page_transitions.windows = ft.PageTransitionTheme.CUPERTINO
    page.fonts = {"Pacifico": "./fonts/Pacifico-Regular.ttf"}

    navbar_settings = {
        "title": "Template",
        "color_bg": ft.Colors.LIGHT_BLUE_ACCENT_700,
        "color_text": ft.Colors.WHITE,
        "items": [
            ft.PopupMenuItem(text="Login"),
            ft.PopupMenuItem(),  # divider
            ft.PopupMenuItem(text="Profile"),
            ft.PopupMenuItem(),  # divider
            ft.PopupMenuItem(text="Settings")
        ]
    }
    layout_settings = {

    }
    navbar = Navbar(page, settings=navbar_settings)
    layout = Layout(navbar, page, layout_settings)
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