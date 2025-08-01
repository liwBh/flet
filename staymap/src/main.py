import flet as ft
import flet_map as map
from config.settings import settings
from app.map_view import create_map
from app.handlers import handle_tap, handle_event, get_markers


def main(page: ft.Page):
    # Aplicar configuración global de Flet (título, fuentes, colores)
    settings.set_settings_app(page)

    # Referencia a capa de marcadores
    marker_layer_ref = ft.Ref[map.MarkerLayer]()

    # Obtener marcadores iniciales
    initial_markers = get_markers(page, marker_layer_ref)

    # Construir el mapa usando nuestra abstracción
    mapa = create_map(
        marker_layer_ref,
        lambda e: handle_tap(e, page, marker_layer_ref),
        handle_event,
        initial_markers=initial_markers
    )

    # Añadir elementos a la página
    page.add(
        ft.Text("Click (tap) para añadir una parada."),
        mapa
    )

if __name__ == "__main__":
    ft.app(target=main)
