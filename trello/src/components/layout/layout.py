import flet as ft
from .sidebar import Sidebar

class Layout(ft.Row):
    def __init__(self, app, page: ft.Page, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = app
        self.page = page
        self.app.appbar.leading.on_click = self.toggle_nav_rail
        self.sidebar = Sidebar(self)
        self._active_view: Control = ft.Column(
            controls=[ft.Text("Active View")],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
        self.controls = [self.sidebar, self.active_view]
        self.expand = True
        self.alignment = ft.alignment.top_center

    @property
    def active_view(self):
        return self._active_view

    @active_view.setter
    def active_view(self, view):
        self._active_view = view
        self.update()

    def toggle_nav_rail(self, e):
        self.sidebar.visible = not self.sidebar.visible
        self.page.update()
