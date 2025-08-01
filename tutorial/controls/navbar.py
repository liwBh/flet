import flet as ft

# Navbar inferior
class NavBar(ft.Container):

    def __init__(self, page):
        super().__init__()
        self.nav_drawer = None
        self.nav_bottom_buttons = None
        self.nav_buttons = None
        self.page = page
        self.navbar_bottom(page)
        self.navbar_drawer()

    def change_tab(self, e: ft.ControlEvent):
        idx = e.control.selected_index
        if idx == 0:
            self.page.go("/row")
        elif idx == 1:
            self.page.go("/container")
        elif idx == 2:
            self.page.go("/card")
        elif idx == 3:
            self.page.go("/theme")


    def navbar_bottom(self, page):
        self.nav_bottom_buttons = ft.NavigationBar(
            bgcolor="#18191b",
            indicator_color=ft.Colors.AMBER,
            destinations=[
                ft.NavigationBarDestination(
                    icon=ft.Icons.COMPARE_ARROWS,
                    selected_icon=ft.Icons.HOME_FILLED,
                    label="Row",
                ),
                ft.NavigationBarDestination(
                    icon=ft.Icons.LOCAL_GROCERY_STORE_OUTLINED,
                    selected_icon=ft.Icons.LOCAL_GROCERY_STORE,
                    label="Container",
                )
            ],
            on_change=self.change_tab,
            selected_index=0,
        )

    # Navbar lateral
    def navbar_drawer(self):
        self.nav_drawer = ft.NavigationDrawer(
            controls=[
                ft.Container(height=12),
                ft.NavigationDrawerDestination(
                    icon=ft.Icons.COMPARE_ARROWS, label="Row"
                ),
                ft.NavigationDrawerDestination(
                    icon=ft.Icons.LOCAL_GROCERY_STORE_OUTLINED, label="Container"
                ),
                ft.NavigationDrawerDestination(
                    icon=ft.Icons.CHECK_BOX_OUTLINE_BLANK_ROUNDED, label="Card"
                ),
                ft.NavigationDrawerDestination(
                    icon=ft.Icons.PALETTE, label="Theme"
                ),
            ],
            on_change=self.change_tab
        )


