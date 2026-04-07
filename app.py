import os

def connect_to_db(username):
    password = os.getenv("DB_PASSWORD") # Безопасно!
    print(f"Connecting user {username} to database...")
