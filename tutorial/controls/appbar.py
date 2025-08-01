import flet as ft

class AppBar(ft.Container):
    def __init__(self, page, navside):
        super().__init__()
        self.page = page
        self.appbar = None
        self.navside = navside
        self.build_appbar()

    def build_appbar(self):
        self.appbar = ft.AppBar(
            leading_width=40,
            title=ft.Text("AppBar Example"),
            center_title=True,
            bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
        )

    def display_sidebar(self, e):
        self.navside.extended = not self.navside.extended
        self.navside.update()

