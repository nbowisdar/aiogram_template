from db.piccolo_conf import *  # noqa


DB = PostgresEngine(
    config={
        "database": "postgres_test",
        "user": "postgres",
        "password": "postgres",
        "host": "localhost",
        "port": 5432,
    }
)
