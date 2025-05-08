# pyqtforge/db/config.py

import sqlite3
from pathlib import Path

# Default database path
DB_PATH = Path("app.db")

def get_connection():
    """Returns a connection to the SQLite database."""
    conn = sqlite3.connect(DB_PATH)
    return conn
