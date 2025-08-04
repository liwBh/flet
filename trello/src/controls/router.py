
import flet as ft

def route_change(self, layout):
    troute = ft.TemplateRoute(self.page.route)
    if troute.match("/"):
        self.page.go("/boards")
    elif troute.match("/board/:id"):
        if int(troute.id) > len(layout.store.get_boards()):
            self.page.go("/")
            return
        layout.set_board_view(int(troute.id))
    elif troute.match("/boards"):
        layout.set_all_boards_view()
    elif troute.match("/members"):
        layout.set_members_view()
    self.page.update()

