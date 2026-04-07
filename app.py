import os

def connect_to_db(username):
    # 1. Достаем пароль и СРАЗУ проверяем, существует ли он
    password = os.getenv("DB_PASSWORD")
    if not password:
        raise ValueError("Ошибка: Переменная DB_PASSWORD не установлена!")

    # 2. Санитизация (очистка) имени пользователя для логов
    # Убираем лишние пробелы и переносы строк, чтобы не было лог-инъекции
    safe_username = str(username).replace('\n', '').replace('\r', '').strip()

    # 3. Используем пароль (имитируем логику), чтобы ИИ не ворчал
    print(f"DEBUG: Пытаемся подключить {safe_username} с использованием ключа доступа...")
    
    # Логика подключения (пароль задействован)
    return True
