
from pyqtforge.db.orm import Model

class Blog(Model):
    table_name = "blog"
    fields = {
        "name": "TEXT",
        "class" : "TEXT",
        "page" : "INT",
        "created_at": "TEXT"
    }
