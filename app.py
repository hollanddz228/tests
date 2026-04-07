import sqlite3

def login_user(username, password):
    # УЯЗВИМОСТЬ 1: Пароль прямо в коде (Hardcoded Credential)
    admin_password = "super_secret_admin_password_123" 
    
    # УЯЗВИМОСТЬ 2: Формирование запроса через f-строку (SQL Injection)
    # Хакер может ввести: admin' --
    db = sqlite3.connect("users.db")
    cursor = db.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    
    print(f"DEBUG: Checking credentials for {username}...")
    cursor.execute(query)
    return cursor.fetchone()
