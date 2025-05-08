# pyqtforge/db/orm.py

from pyqtforge.db.config import get_connection

class Model:
    table_name = ""
    fields = {}

    @classmethod
    def create_table(cls):
        columns = ", ".join([f"{name} {type_}" for name, type_ in cls.fields.items()])
        query = f"CREATE TABLE IF NOT EXISTS {cls.table_name} (id INTEGER PRIMARY KEY AUTOINCREMENT, {columns})"

        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()

    @classmethod
    def insert(cls, **kwargs):
        keys = ", ".join(kwargs.keys())
        placeholders = ", ".join(["?" for _ in kwargs])
        values = list(kwargs.values())
        query = f"INSERT INTO {cls.table_name} ({keys}) VALUES ({placeholders})"

        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, values)
            conn.commit()

    @classmethod
    def all(cls):
        query = f"SELECT * FROM {cls.table_name}"
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            return cursor.fetchall()
