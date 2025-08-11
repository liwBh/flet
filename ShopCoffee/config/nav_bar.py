

import flet as ft


class NavBar(ft.Container):
    def __init__(self, page):
        super().__init__(
            bgcolor="#18191b",
            alignment=ft.alignment.center,
            border_radius=10,
            padding=0,
            height=50,
            margin=ft.margin.only(top=5),

        )
        self.color_coffe = "#b9894b"
        self.page = page


        self.nav_buttons = ft.NavigationBar(
            bgcolor="#18191b",
            indicator_color=self.color_coffe,
            destinations=[
                ft.NavigationBarDestination(
                    icon=ft.Icons.HOME_OUTLINED,
                    selected_icon=ft.Icons.HOME_FILLED,
                    label="Home",
                ),
                ft.NavigationBarDestination(
                    icon=ft.Icons.LOCAL_GROCERY_STORE_OUTLINED,
                    selected_icon=ft.Icons.LOCAL_GROCERY_STORE,
                    label="Store",
                ),
                ft.NavigationBarDestination(
                    icon=ft.Icons.FAVORITE_BORDER,
                    selected_icon=ft.Icons.FAVORITE,
                    label="Favorites",
                ),
                ft.NavigationBarDestination(
                    icon=ft.Icons.NOTIFICATIONS_NONE,
                    selected_icon=ft.Icons.NOTIFICATIONS,
                    label="Notifications",
                ),
            ],
            on_change=self.change_tab,
            selected_index=0,
        )

    def change_tab(self, e: ft.ControlEvent):
        idx = e.control.selected_index
        if idx == 0:
            self.page.go("/home")
        elif idx == 1:
            self.page.go("/store")
        elif idx == 2:
            self.page.go("/favorites")
        elif idx == 3:
            self.page.go("/notifications")

