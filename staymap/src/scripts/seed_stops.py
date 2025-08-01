"""
Script para sembrar paradas de autobús por defecto en la base de datos.
Ejecutar:
    python -m database.seed_stops
"""
from database.db import engine
from sqlmodel import Session
from database.cruds import create_stop, delete_stop, get_stops

# Lista de paradas por defecto: (nombre, latitud, longitud)
default_stops = [
    ("Parada A", 30.0, 15.0),
    ("Parada B", 10.0, 10.0),
    ("Parada C", 25.0, 45.0),
]

if __name__ == "__main__":
    # Crear las paradas por defecto
    for name, lat, lng in default_stops:
        create_stop(name=name, lat=lat, lng=lng)
        print(f"✅ Parada creada: {name} @ ({lat}, {lng})")

    print("🌱 Seed de paradas completado.")