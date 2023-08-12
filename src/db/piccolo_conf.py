from piccolo.engine.postgres import PostgresEngine

from piccolo.conf.apps import AppRegistry

DB = PostgresEngine(
    config={
        "database": "db",
        "user": "postgres",
        "password": "1324",
        "host": "localhost",
        "port": 5433,
    }
)

APP_REGISTRY = AppRegistry(apps=["home.piccolo_app", "piccolo_admin.piccolo_app"])
