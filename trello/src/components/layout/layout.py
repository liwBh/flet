import flet as ft
from components.layout.sidebar import Sidebar

class Layout(ft.Row):
    def __init__(self, navbar, page: ft.Page, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.navbar = navbar
        self.page = page
        self.navbar.appbar.leading.on_click = self.toggle_nav_rail
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

    def set_board_view(self, i):
        #self.active_view = self.store.get_boards()[i]
        self.sidebar.top_nav_rail.selected_index = None
        self.page_resize()
        self.page.update()
        pass

    def set_all_boards_view(self):
        #self.active_view = self.all_boards_view
        #self.hydrate_all_boards_view()
        self.sidebar.top_nav_rail.selected_index = 0
        self.page.update()


    def set_members_view(self):
        #self.active_view = self.members_view
        self.sidebar.top_nav_rail.selected_index = 1
        self.page.update()

    def toggle_nav_rail(self, e):
        self.sidebar.visible = not self.sidebar.visible
        self.page.update()
