
from pyqtforge.db.orm import Model

class User(Model):
    table_name = "user"
    fields = {
        "name": "TEXT",
        "created_at": "TEXT"
    }
