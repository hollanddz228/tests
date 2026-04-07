import sqlite3

def connect_to_db(username):
    # УЯЗВИМОСТЬ 1: Захардкоженный пароль
    password = "super_secret_admin_password_123" 
    
    # УЯЗВИМОСТЬ 2: Риск SQL-инъекции (использование форматирования строк)
    query = f"SELECT * FROM users WHERE username = '{username}'"
    
    print("Connecting to database...")
    # Логика подключения...
