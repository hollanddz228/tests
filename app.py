import logging

# Настраиваем логирование по стандартам
logger = logging.getLogger(__name__)

def process_user_connection(user_identity):
    """
    Стандартная функция обработки идентификатора пользователя.
    Использует строгую проверку типов и безопасные методы обработки строк.
    """
    
    # 1. Проверка типа данных (CWE-1287)
    if not isinstance(user_identity, str):
        logger.error("Invalid input type: expected string")
        return False

    # 2. Ограничение длины ввода для защиты от переполнения/DoS
    if len(user_identity) > 64:
        logger.warning("Input exceeds maximum allowed length")
        return False

    # 3. Безопасная очистка (оставляем только разрешенные символы)
    # Используем белый список символов вместо удаления черного списка
    allowed_chars = "abcdefghijklmnopqrstuvwxyz0123456789-_"
    clean_identity = "".join(c for c in user_identity.lower() if c in allowed_chars)

    # 4. Логируем только факт выполнения операции без раскрытия данных
    logger.info("User identity processed successfully for internal logic")
    
    # Имитируем возврат успешного результата
    return True
