from typing import List

import flet as ft
import flet_map as map
from flet.core.cupertino_colors import CupertinoColors
from database.cruds import create_stop, delete_stop, get_stops, get_stop


def open_dialog_name(
    e: map.MapTapEvent,
    page: ft.Page,
    marker_layer_ref: ft.Ref[map.MarkerLayer]
):
    """
    Abre un diálogo modal para ingresar el nombre de la parada.
    """
    name_field = ft.TextField(label="Nombre de la parada", width=200)

    # Definimos el diálogo con acciones
    dlg = ft.AlertDialog(
        title=ft.Text("Ingrese nombre de la parada"),
        content=name_field,
        alignment=ft.alignment.center,
        actions=[
            ft.TextButton("Cancelar", on_click=lambda ev: page.close(dlg)),
            ft.ElevatedButton("Guardar", on_click=lambda ev: save_and_add(ev, page, e, name_field, marker_layer_ref, dlg))
        ],
        on_dismiss=lambda ev: page.close(dlg)
    )

    page.open(dlg)
    page.update()


def save_and_add(
    ev: ft.ControlEvent,
    page: ft.Page,
    e: map.MapTapEvent,
    name_field: ft.TextField,
    marker_layer_ref: ft.Ref[map.MarkerLayer],
    dlg: ft.AlertDialog
):
    # Cerrar diálogo
    page.close(dlg)
    page.update()

    # Obtener nombre
    name = name_field.value.strip() or "Parada"

    # Crear el registro en la base de datos
    new_stop = create_stop(
        name=name,
        lat=e.coordinates.latitude,
        lng=e.coordinates.longitude
    )

    # Crear marcador con IconButton como contenido interactivo
    btn =  ft.IconButton(
            icon=ft.Icons.LOCATION_ON,
            icon_color=CupertinoColors.DESTRUCTIVE_RED,
            tooltip=ft.Tooltip(
                message=name,
                bgcolor=ft.Colors.BLACK,
                text_style=ft.TextStyle(size=20, color=ft.Colors.WHITE),
            )
        )

    marker = map.Marker(
        btn,
        coordinates=e.coordinates,
        data=new_stop.id
    )

    btn.on_click = lambda ev, m=marker: handle_remove(ev, page, marker_layer_ref, m)

    # Añadimos marcador a la capa
    marker_layer_ref.current.markers.append(marker)
    page.update()


def handle_tap(
    e: map.MapTapEvent,
    page: ft.Page,
    marker_layer_ref: ft.Ref[map.MarkerLayer]
):
    """
    Añade un marcador al hacer tap en el mapa
    """
    if e.name != "tap":
        return

    open_dialog_name(e, page, marker_layer_ref)

def delete_marker(

        #e: map.MapTapEvent,
        page: ft.Page,
        marker_layer_ref: ft.Ref[map.MarkerLayer],
        marker: map.Marker,
        dlg: ft.AlertDialog
):
    stop_id = marker.data

    if delete_stop(stop_id):
        marker_layer_ref.current.markers.remove(marker)
        page.update()
    else:
        page.snack_bar = ft.SnackBar(ft.Text("Error: no se pudo eliminar la parada"))
        page.snack_bar.open = True
        page.update()
    page.close(dlg)

def handle_remove(
    e: ft.ControlEvent,
    page: ft.Page,
    marker_layer_ref: ft.Ref[map.MarkerLayer],
    marker: map.Marker
):
    """
    Elimina el marcador asociado al IconButton clicado.
    """
    marker_name = get_stop(marker.data).name
    dlg = ft.AlertDialog(
        title=ft.Text("Eliminar parada"),
        content=ft.Text(f"¿Estás seguro de que deseas eliminar esta parada: {marker_name}?"),
        actions=[
            ft.TextButton("Cancelar", on_click=lambda ev: page.close(dlg)),
            ft.ElevatedButton("Eliminar", on_click=lambda ev: delete_marker(page, marker_layer_ref,marker, dlg), bgcolor=ft.Colors.RED)
        ],
        on_dismiss=lambda ev: page.close(dlg)
    )
    page.open(dlg)
    page.update()


def get_markers(
    page: ft.Page,
    marker_layer_ref: ft.Ref[map.MarkerLayer]
) -> List[map.Marker]:
    """
    Construye una lista de marcadores desde la BD, con eventos de eliminación.
    """
    initial_markers: List[map.Marker] = []
    for stop in get_stops():
        coords = map.MapLatitudeLongitude(stop.lat, stop.lng)
        # Crear marcador con IconButton como contenido interactivo

        btn = ft.IconButton(
            icon=ft.Icons.LOCATION_ON,
            icon_color=CupertinoColors.DESTRUCTIVE_RED,
            tooltip=ft.Tooltip(
                message=stop.name,
                bgcolor=ft.Colors.BLACK,
                text_style=ft.TextStyle(size=20, color=ft.Colors.WHITE),
            )
        )

        marker = map.Marker(
            btn,
            coordinates=coords,
            data=stop.id
        )
        btn.on_click = lambda ev, m=marker: handle_remove(ev, page, marker_layer_ref, marker)
        initial_markers.append(marker)
    return initial_markers


def handle_event(e: map.MapEvent):
    """
    Registro de eventos genéricos del mapa.
    """
    print(e)
