import flet as ft
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from router.router import router
from router.views import Views
from controls.navbar import NavBar
from controls.appbar import AppBar

class AppTutorial(ft.Container):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.views = Views(page=self.page).views
        self.navbar = NavBar(self.page)
        self.appbar = AppBar(page=self.page, navside=self.navbar.nav_drawer)
        self.build_view()

    def build_view(self):
        self.page.drawer = self.navbar.nav_drawer
        self.page.appbar = self.appbar.appbar
        self.page.navigation_bar = self.navbar.nav_bottom_buttons
        self.page.on_route_change = lambda r: router(self, self.page.route, self.views)
        self.page.go("/row")



ft.app(target=AppTutorial)