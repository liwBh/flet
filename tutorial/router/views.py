
from views.card import build_view_card
from views.container import build_view_container
from views.row import build_view_row
from views.theme import build_view_theme

class Views:
    def __init__(self, page):
        self.page = page
        self.views = [
            {"route": "/row", "view": build_view_row(page=self.page)},
            {"route": "/container", "view": build_view_container(page=self.page)},
            {"route": "/card", "view": build_view_card()},
            {"route": "/theme", "view": build_view_theme(page=self.page)},
        ]
