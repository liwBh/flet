import flet as ft

class Navbar:
    def __init__(self, page: ft.Page, settings: dict):
        self.page = page
        self.action = None
        self.appbar_items = settings.get("items", [])
        self.appbar = ft.AppBar(

            leading=ft.IconButton(icon=ft.Icons.MENU),
            leading_width=100,
            title=ft.Text(settings.get("title"), size=32, color=settings.get("color_text"), text_align=ft.TextAlign.START),
            center_title=False,
            toolbar_height=75,
            bgcolor=settings.get("color_bg"),
            actions=[
                ft.Container(
                    content=ft.PopupMenuButton(
                        items=self.appbar_items
                    ),
                    margin=ft.margin.only(left=50, right=25)
                )
            ],
        )
        self.page.appbar = self.appbar
        self.page.update()

    def action(self, action):
        self.action = action

