from typing import List, Optional
from sqlmodel import Session, select

from database.db import engine
from database.models import Stop #, Route, RouteStop, Bus

# ----------------------
# CRUD para Stop
# ----------------------

def create_stop(name: str, lat: float, lng: float) -> Stop:
    with Session(engine) as session:
        stop = Stop(name=name, lat=lat, lng=lng)
        session.add(stop)
        session.commit()
        session.refresh(stop)
        return stop


def get_stop(stop_id: int) -> Optional[Stop]:
    with Session(engine) as session:
        return session.get(Stop, stop_id)


def get_stops() -> List[Stop]:
    with Session(engine) as session:
        return session.exec(select(Stop)).all()


def update_stop(stop_id: int, name: Optional[str] = None, lat: Optional[float] = None, lng: Optional[float] = None) -> Optional[Stop]:
    with Session(engine) as session:
        stop = session.get(Stop, stop_id)
        if not stop:
            return None
        if name is not None:
            stop.name = name
        if lat is not None:
            stop.lat = lat
        if lng is not None:
            stop.lng = lng
        session.add(stop)
        session.commit()
        session.refresh(stop)
        return stop


def delete_stop(stop_id: int) -> bool:
    with Session(engine) as session:
        stop = session.get(Stop, stop_id)
        if not stop:
            return False
        session.delete(stop)
        session.commit()
        return True

# ----------------------
# CRUD para Route
# ----------------------

# def create_route(name: str) -> Route:
#     with Session(engine) as session:
#         route = Route(name=name)
#         session.add(route)
#         session.commit()
#         session.refresh(route)
#         return route
#
#
# def get_route(route_id: int) -> Optional[Route]:
#     with Session(engine) as session:
#         return session.get(Route, route_id)
#
#
# def get_routes() -> List[Route]:
#     with Session(engine) as session:
#         return session.exec(select(Route)).all()
#
#
# def update_route(route_id: int, name: Optional[str] = None) -> Optional[Route]:
#     with Session(engine) as session:
#         route = session.get(Route, route_id)
#         if not route:
#             return None
#         if name is not None:
#             route.name = name
#         session.add(route)
#         session.commit()
#         session.refresh(route)
#         return route
#
#
# def delete_route(route_id: int) -> bool:
#     with Session(engine) as session:
#         route = session.get(Route, route_id)
#         if not route:
#             return False
#         session.delete(route)
#         session.commit()
#         return True
#
# # -------------------------
# # CRUD para RouteStop
# # -------------------------
#
# def add_stop_to_route(route_id: int, stop_id: int, sequence: int) -> RouteStop:
#     with Session(engine) as session:
#         rel = RouteStop(route_id=route_id, stop_id=stop_id, sequence=sequence)
#         session.add(rel)
#         session.commit()
#         session.refresh(rel)
#         return rel
#
#
# def get_route_stops(route_id: int) -> List[RouteStop]:
#     with Session(engine) as session:
#         return session.exec(
#             select(RouteStop)
#             .where(RouteStop.route_id == route_id)
#             .order_by(RouteStop.sequence)
#         ).all()
#
#
# def delete_route_stop(route_id: int, stop_id: int) -> bool:
#     with Session(engine) as session:
#         rel = session.get(RouteStop, (route_id, stop_id))
#         if not rel:
#             return False
#         session.delete(rel)
#         session.commit()
#         return True
#
# # ----------------------
# # CRUD para Bus
# # ----------------------
#
# def create_bus(name: str, route_id: int, active: bool = True) -> Bus:
#     with Session(engine) as session:
#         bus = Bus(name=name, route_id=route_id, active=active)
#         session.add(bus)
#         session.commit()
#         session.refresh(bus)
#         return bus
#
#
# def get_bus(bus_id: int) -> Optional[Bus]:
#     with Session(engine) as session:
#         return session.get(Bus, bus_id)
#
#
# def get_buses(active_only: bool = False) -> List[Bus]:
#     with Session(engine) as session:
#         query = select(Bus)
#         if active_only:
#             query = query.where(Bus.active)
#         return session.exec(query).all()
#
#
# def update_bus(bus_id: int, name: Optional[str] = None, route_id: Optional[int] = None, active: Optional[bool] = None) -> Optional[Bus]:
#     with Session(engine) as session:
#         bus = session.get(Bus, bus_id)
#         if not bus:
#             return None
#         if name is not None:
#             bus.name = name
#         if route_id is not None:
#             bus.route_id = route_id
#         if active is not None:
#             bus.active = active
#         session.add(bus)
#         session.commit()
#         session.refresh(bus)
#         return bus
#
#
# def delete_bus(bus_id: int) -> bool:
#     with Session(engine) as session:
#         bus = session.get(Bus, bus_id)
#         if not bus:
#             return False
#         session.delete(bus)
#         session.commit()
#         return True
