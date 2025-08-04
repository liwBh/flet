import flet as ft
from components.layout.navbar import Navbar
from components.layout.layout import Layout
from controls.router.views import Views
from controls.router.router import router

class AppTemplate(ft.Container):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.views = Views(page=self.page).views
        self.navbar = Navbar(page, settings=self.navbar_settings())
        self.layout = Layout(self.navbar, page, self.layout_settings())
        container = ft.Container(
            bgcolor=ft.Colors.WHITE,
            content=self.layout,
            expand=True,
            alignment=ft.alignment.top_center,
        )
        page.add(container)
        page.update()
        self.build_view()

    def build_view(self):
        self.page.title = "Template"
        self.page.padding = 0
        self.page.bgcolor = ft.Colors.BLUE_GREY_500
        self.page.theme = ft.Theme(font_family="Verdana")
        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.theme.page_transitions.windows = ft.PageTransitionTheme.CUPERTINO
        self.page.fonts = {"Pacifico": "./fonts/Pacifico-Regular.ttf"}
        self.page.on_route_change = lambda r: router(self, self.page.route, self.views, self.layout)
        self.page.go("/")

    def navbar_settings(self):
        return {
            "title": "Template",
            "color_bg": ft.Colors.LIGHT_BLUE_ACCENT_700,
            "color_text": ft.Colors.WHITE,
            "items": [
                ft.PopupMenuItem(text=v.name, data=v.route, icon=v.icon, on_click=lambda e: self.redirect_navbar(e))
                for v in self.views if v.position == 0
            ]
        }

    def redirect_navbar(self, e):
        self.page.go(e.control.data)

    def layout_settings(self):
        return {

        }

if __name__ == "__main__":
    ft.app(target=AppTemplate, assets_dir="./assets")