import flet as ft
from src.components.layout.sidebar import Sidebar


class Layout(ft.Row):
    def __init__(self, navbar, page: ft.Page, settings: dict, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.navbar = navbar
        self.page = page
        self.page_content = ft.Text("Home", color=settings.get("color_text"), size=20)
        self.navbar.appbar.leading.on_click = self.toggle_nav_rail
        self.sidebar = Sidebar(self)
        self._active_view: Control = ft.Column(
            controls=[self.page_content],
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

    def update_view(self, view):
        self.page_content = view
        self.update()

