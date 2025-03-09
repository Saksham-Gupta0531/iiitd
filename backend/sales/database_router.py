class DatabaseRouter:
    """
    A router to control database operations for multiple databases.
    """

    def db_for_read(self, model, **hints):
        """Point database reads to the correct database."""
        if model._meta.db_table == "mysql_salesdata":
            return "mysql"
        elif model._meta.db_table == "postgres_salesdata":
            return "postgresql"
        return "default"  # SQLite

    def db_for_write(self, model, **hints):
        """Point database writes to the correct database."""
        if model._meta.db_table == "mysql_salesdata":
            return "mysql"
        elif model._meta.db_table == "postgres_salesdata":
            return "postgresql"
        return "default"  # SQLite

    def allow_relation(self, obj1, obj2, **hints):
        """Allow relations if both models are in the same database."""
        db_set = {"default", "mysql", "postgresql"}
        if obj1._state.db in db_set and obj2._state.db in db_set:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Ensure migrations apply only to the correct database."""
        if app_label == "sales":  # Updated app name
            if model_name == "mysqlsalesdata" and db == "mysql":
                return True
            elif model_name == "postgressalesdata" and db == "postgresql":
                return True
            elif model_name == "salesdata" and db == "default":
                return True
        return False
