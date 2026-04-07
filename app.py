import logging

# Настройка логирования без раскрытия инфраструктуры
logger = logging.getLogger(__name__)

def process_data_request(input_string):
    """
    Безопасная обработка входящих данных.
    """
    # 1. Проверка типа данных
    if not isinstance(input_string, str):
        return False

    # 2. Ограничение длины (Защита от переполнения)
    if len(input_string) > 32:
        return False

    # 3. Валидация через белый список (Только буквы и цифры)
    if not input_string.isalnum():
        logger.warning("Invalid characters detected in input")
        return False

    # 4. Безопасный вывод
    logger.info("Data processing completed successfully")
    return True
