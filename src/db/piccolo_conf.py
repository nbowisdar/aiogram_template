from piccolo.conf.apps import AppRegistry
from piccolo.engine.postgres import PostgresEngine

DB = PostgresEngine(
    config={
        "database": "dev",
        "user": "postgres",
        "password": "1324",
        "host": "localhost",
        "port": 5432,
    }
)

APP_REGISTRY = AppRegistry(
    apps=["src.db.home.piccolo_app", "piccolo_admin.piccolo_app"]
)
