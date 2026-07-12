import sqlite3
from fastapi import FastAPI

conn = sqlite3.connect("data.db", check_same_thread=False)

cursor = conn.cursor()
app = FastAPI()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT NOT NULL,
        tiltle TEXT
    )
""")

conn.commit()

@app.get("/")
def root():
    return {"message": "sql lite working"}