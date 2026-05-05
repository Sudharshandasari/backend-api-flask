import sqlite3 

DB_NAME = "app.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        input_data TEXT,
        k INTEGER,
        result INTEGER
    )
    """)

    conn.commit()
    conn.close()


def insert_result(input_data, k, result):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO results (input_data, k, result)
        VALUES (?, ?, ?)
        """, (str(input_data), k, result))
        conn.commit()
    finally:
        conn.close()