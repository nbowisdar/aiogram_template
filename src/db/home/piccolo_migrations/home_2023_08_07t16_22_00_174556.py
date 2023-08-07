from piccolo.apps.migrations.auto.migration_manager import MigrationManager


ID = "2023-08-07T16:22:00:174556"
VERSION = "0.119.0"
DESCRIPTION = ""


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="home", description=DESCRIPTION
    )

    manager.rename_column(
        table_class_name="Order",
        tablename="order",
        old_column_name="date",
        new_column_name="created_at",
        old_db_column_name="date",
        new_db_column_name="created_at",
    )

    return manager
