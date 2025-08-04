import flet as ft
from components.layout.navbar import Navbar
from components.layout.layout import Layout

def main(page: ft.Page):
    page.title = "Flet Trello clone"
    page.padding = 0
    page.bgcolor = ft.Colors.BLUE_GREY_500
    Navbar(page)
    app = Navbar(page)
    layout = Layout(app, page)
    container = ft.Container(
        content=layout,
        expand=True,
        alignment=ft.alignment.top_center,
        padding=ft.padding.all(20),
    )
    page.add(container)
    page.update()


if __name__ == "__main__":
    ft.app(main)