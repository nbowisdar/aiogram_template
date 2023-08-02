from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from src.config import settings
from src.data.models import Base

# SQLite variant
engine = create_engine(f"sqlite:///db.sqlite3")

# POSTGRES_VARIANT
# engine = create_engine(
#     f"postgresql+psycopg2://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"
# )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_tables():
    # Create a MetaData object
    Base.metadata.create_all(engine)
