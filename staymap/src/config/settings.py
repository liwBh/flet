from pydantic_settings import BaseSettings
import flet as ft
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseSettings):
    TITLE: str = "Stay Map"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "")
    FONTS: dict = {}
    COLORS: dict = {}

    def set_settings_app(self, page: ft.Page):
        page.title = self.TITLE
        page.fonts = self.FONTS
        page.update()

# Instancia global
settings = Settings()
