from typing import List, Optional
from sqlmodel import SQLModel, Field, Relationship


class Stop(SQLModel, table=True):
    """Parada de autobús """
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    lat: float
    lng: float

    # Relación inversa a RouteStop
    # route_stops: List["RouteStop"] = Relationship(back_populates="stop")


# class Route(SQLModel, table=True):
#     """Ruta de autobús"""
#     id: Optional[int] = Field(default=None, primary_key=True)
#     name: str
#
#     # Relación inversa a RouteStop
#     route_stops: List["RouteStop"] = Relationship(back_populates="route")
#
#
# class RouteStop(SQLModel, table=True):
#     """Tabla de unión que define el orden de las paradas en cada ruta"""
#     route_id: int = Field(foreign_key="route.id", primary_key=True)
#     stop_id: int = Field(foreign_key="stop.id", primary_key=True)
#     sequence: int  # posición de la parada en la ruta
#
#     # Relaciones a las dos tablas padre
#     route: "Route" = Relationship(back_populates="route_stops")
#     stop: "Stop" = Relationship(back_populates="route_stops")
#
#
# class Bus(SQLModel, table=True):
#     """Autobús asignado a una ruta"""
#     id: Optional[int] = Field(default=None, primary_key=True)
#     name: str
#     route_id: int = Field(foreign_key="route.id")
#     active: bool = Field(default=True)
#
#     # Opcional: relación a la ruta
#     route: Optional[Route] = Relationship()
