import flet as ft


def router(self, route, views):
    content = next((v["view"] for v in views if v["route"] == route), views[0]["view"])
    self.page.controls.clear()
    self.page.add(
        ft.Column(
            expand=True,
            controls=[
                ft.Container(expand=True, content=content),
            ],
        )
    )
    self.page.update()
