import flet as ft
import flet_map as map
from typing import Optional, List


def create_map(
    marker_layer_ref: ft.Ref[map.MarkerLayer],
    on_tap,
    on_event,
    initial_markers: Optional[List[map.Marker]] = None
) -> map.Map:
    """
    Construye y retorna un mapa configurado con marcadores persistentes y removibles.
    """
    markers = initial_markers or []


    return map.Map(
        expand=True,
        initial_center=map.MapLatitudeLongitude(10.01464, -84.13605),
        initial_zoom=15,
        interaction_configuration=map.MapInteractionConfiguration(
            flags=map.MapInteractiveFlag.ALL
        ),
        on_init=lambda e: print("Map initialized"),
        on_tap=on_tap,
        on_event=on_event,
        layers=[
            # Capa de teselas OpenTopoMap
            map.TileLayer(
                url_template="http://{s}.opentopomap.org/{z}/{x}/{y}.png",
                on_image_error=lambda e: print("TileLayer Error")
            ),
            # Atribuciones de fuente
            map.RichAttribution(
                attributions=[
                    map.TextSourceAttribution(
                        text="OpenStreetMap Contributors",
                        on_click=lambda e: e.page.launch_url(
                            "https://openstreetmap.org/copyright"
                        )
                    ),
                    map.TextSourceAttribution(
                        text="Flet",
                        on_click=lambda e: e.page.launch_url("https://flet.dev")
                    ),
                ]
            ),
            map.SimpleAttribution(
                text="StayMap",
                alignment=ft.alignment.top_right,
                on_click=lambda e: print("Clicked SimpleAttribution")
            ),

            # Capa de marcadores
            map.MarkerLayer(ref=marker_layer_ref, markers=markers),
        ]
    )
