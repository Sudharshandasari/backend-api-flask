from db.database import get_connection
conn = get_connection()
print("Database Connection successful")
conn.close()