import flet as ft
from config import configPage
from views.home import page_home

async def main(page):
    configPage.init(page)
    await page_home(page)
    page.update()

ft.app(target=main)