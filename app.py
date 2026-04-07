import logging

# Настройка логирования
logger = logging.getLogger(__name__)

def validate_user_input(raw_input):
    """
    Финальная версия функции с полной валидацией и проверкой целостности данных.
    """
    # 1. Строгая проверка типа
    if not isinstance(raw_input, str):
        return False

    # 2. Жесткое ограничение длины
    if not (0 < len(raw_input) <= 64):
        return False

    # 3. Белый список разрешенных символов
    allowed_chars = "abcdefghijklmnopqrstuvwxyz0123456789-_"
    
    # Создаем очищенную версию
    sanitized_input = "".join(c for c in raw_input.lower() if c in allowed_chars)

    # 4. КРИТИЧЕСКАЯ ПРОВЕРКА: Если очищенная строка не совпадает с исходной,
    # значит в исходной был недопустимый контент. БЛОКИРУЕМ.
    if raw_input.lower() != sanitized_input:
        logger.warning("Data integrity check failed: unauthorized characters detected")
        return False

    # 5. Только если данные ИДЕАЛЬНО чистые, разрешаем работу
    logger.info("Input validation successful: all security constraints met")
    return True
