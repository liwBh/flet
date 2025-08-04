
import flet as ft

from dataclasses import dataclass
from views.home_view import build_view_home

position = {
    "top": 0,
    "side": 1,
    "bottom": 2,
}

@dataclass
class RouteView:
    name: str
    route: str
    icon: str
    view: ft.Container()
    position: int

class Views:
    def __init__(self, page):
        self.views = [
            RouteView("Inicio", "/", ft.Icons.HOME, build_view_home(page), position["side"]),
            RouteView("Boards", "/boards", ft.Icons.CONTACTS, ft.Container(content=ft.Text("Boards")), position["side"]),
            RouteView("Members", "/members", ft.Icons.PERSON, ft.Container(content=ft.Text("Members")), position["side"]),
            RouteView("Login", "/login", ft.Icons.LOGIN, ft.Container(content=ft.Text("Login")), position["top"]),
            RouteView("Profile", "/profile", ft.Icons.PERSON, ft.Container(content=ft.Text("Profile")), position["top"]),
            RouteView("Settings", "/settings", ft.Icons.SETTINGS, ft.Container(content=ft.Text("Settings")), position["top"]),
        ]
