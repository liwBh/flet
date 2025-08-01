from sqlmodel import create_engine
from config.settings import settings

engine = create_engine(
    settings.DATABASE_URL,
    echo=True,
    connect_args={"options": "-c timezone=utc"}
)