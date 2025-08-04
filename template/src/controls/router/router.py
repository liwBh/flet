import flet as ft


def router(self, route, views, layout):
    # Busca en la lista de vistas la que coincida con la ruta actual; si no encuentra ninguna, usa la primera por defecto
    content = next((v.view for v in views if v.route == route), views[0].view)

    # Limpia todos los controles actuales de la página
    # self.page.controls.clear()

    # Actualiza el contenido de la página
    layout.update_view(content)

    # Actualiza la interfaz de la página para reflejar los cambios
    self.page.update()
