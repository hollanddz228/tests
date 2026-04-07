import logging
import re

logger = logging.getLogger(__name__)

def get_safe_user_id(input_data):
    """
    Максимально безопасная валидация. 
    Возвращает очищенную строку или None, если ввод недопустим.
    """
    # 1. Строгая проверка типа (никаких скрытых вызовов __str__)
    if type(input_data) is not str:
        return None

    # 2. Ограничение длины
    if not (0 < len(input_data) <= 64):
        return None

    # 3. Регулярное выражение (White-list)
    # Разрешаем СТРОГО только латиницу a-z, A-Z, цифры 0-9, тире и подчеркивание.
    # Никакого приведения регистров до проверки!
    pattern = re.compile(r'^[a-zA-Z0-9_-]+$')
    
    if not pattern.match(input_data):
        logger.warning("Security alert: Blocked input with unauthorized characters")
        return None

    # 4. Возвращаем саму проверенную строку. 
    # Теперь вызывающий код гарантированно работает с валидными данными.
    return input_data

# Для Jenkins нам нужно, чтобы функция возвращала True/False для статуса
def validate_for_ci(data):
    result = get_safe_user_id(data)
    return result is not None
