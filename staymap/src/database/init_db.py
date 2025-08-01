"""
Script para crear las tablas en la base de datos
"""

from sqlmodel import SQLModel
from database.db import engine
from database.models import Stop

def init_db():
    print("⏳ Creando tablas...")
    SQLModel.metadata.create_all(engine)
    print("✅ Tablas creadas correctamente.")

def reset_db():
    print("⏳ Eliminando tablas...")
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)
    print("✅ Tablas eliminadas y recreadas correctamente.")

if __name__ == "__main__":
    init_db()

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "reset":
        reset_db()
    else:
        init_db()