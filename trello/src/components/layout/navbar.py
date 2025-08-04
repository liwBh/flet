import flet as ft

class Navbar:
    def __init__(self, page: ft.Page):
        self.page = page
        self.action = None
        self.appbar_items = [
            ft.PopupMenuItem(text="Login"),
            ft.PopupMenuItem(),  # divider
            ft.PopupMenuItem(text="Settings")
        ]
        self.appbar = ft.AppBar(

            leading=ft.IconButton(icon=ft.Icons.MENU),
            leading_width=100,
            title=ft.Text("Trello", size=32, text_align=ft.TextAlign.START),
            center_title=False,
            toolbar_height=75,
            bgcolor=ft.Colors.LIGHT_BLUE_ACCENT_700,
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

