import flet as ft
from flet import (Page, TextField, ElevatedButton, Column, Text,
                  Row, Colors, Dropdown, dropdown, Container)

from dotenv import load_dotenv
import requests
import os

load_dotenv()
WEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city):
    """Obtener la información del clima para una ciudad"""
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            temp = data["main"]["temp"]
            description = data["weather"][0]["description"]
            return f"El clima en {city} es {description} con temperatura de {temp} °C"
        else:
            return f"Error al obtener el clima: {data.get('message', 'Ciudad no encontrada')}"

    except Exception as e:
        return f"Error al obtener el clima: {str(e)}"

def main(page: Page):
    page.title = "Consultar clima con flet"
    page.bgcolor = Colors.GREY_900
    page.theme_mode = "Dark"

    input_box = TextField(
        label="Pregunta el clima de tu ciudad favorita",
        border_color=Colors.BLUE_200,
        focused_border_color=Colors.BLUE_400,
        text_style=ft.TextStyle(color=Colors.WHITE),
        expand=True,
    )

    chat_area = ft.Column(
        scroll="auto",
        expand=True,
        horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
    )
    def send_message(e):
        user_message = input_box.value.lower().strip()

        if not user_message:
            return

        chat_area.controls.append(Text(f"Usuario: {user_message}", color=Colors.WHITE))
        response = get_weather(user_message)
        chat_area.controls.append(Text(f"Chatbot: {response}", color=Colors.WHITE))
        input_box.value = ""
        page.update()

    send_button = ElevatedButton(
        "Enviar",
        on_click=send_message,
        bgcolor=Colors.BLUE_700,
        color=Colors.WHITE,
        style=ft.ButtonStyle(padding=ft.padding.symmetric(horizontal=25, vertical=10))
    )

    # enviar mensaje cuando presiona enter
    input_box.on_submit = send_message

    chat_container = Container(
        content=chat_area,
        bgcolor=Colors.BLUE_GREY_900,
        padding=10,
        border_radius=10,
        expand=True,
    )

    input_container = Container(
        content=Row(
            controls=[
                input_box,
                send_button,
            ],
            spacing=10,
        )
    )

    page.add(chat_container, input_container)

    page.window.width = 800
    page.window.height = 600
    page.update()


if __name__ == "__main__":
    ft.app(target=main)