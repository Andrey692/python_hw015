# Задание 1. Логирование с использованием нескольких файлов.
# Напишите скрипт, который логирует разные типы сообщений в разные файлы.
# Логи уровня DEBUG и INFO должны сохраняться в debug_info.log, а логи уровня
# WARNING и выше — в warnings_errors.log.

import logging

# Создаем два логгера: один для DEBUG и INFO, другой для WARNING и выше
debug_info_logger = logging.getLogger("debug_info")
warnings_errors_logger = logging.getLogger("warnings_errors")

# Устанавливаем уровни логирования
debug_info_logger.setLevel(logging.DEBUG)
warnings_errors_logger.setLevel(logging.WARNING)

# Создаем обработчики для записи в разные файлы
debug_info_handler = logging.FileHandler("debug_info.log", encoding="utf-8")
warnings_errors_handler = logging.FileHandler("warnings_errors.log", encoding="utf-8")

# Устанавливаем уровни для обработчиков
debug_info_handler.setLevel(logging.DEBUG)
warnings_errors_handler.setLevel(logging.WARNING)

# Создаем форматтер для логов
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

debug_info_handler.setFormatter(formatter)
warnings_errors_handler.setFormatter(formatter)

# Добавляем обработчики к логгерам
debug_info_logger.addHandler(debug_info_handler)
warnings_errors_logger.addHandler(warnings_errors_handler)

# Логируем примеры сообщений
def log_messages():
    debug_info_logger.debug("Это отладочное сообщение.")
    debug_info_logger.info("Это информационное сообщение.")
    warnings_errors_logger.warning("Это предупреждение.")
    warnings_errors_logger.error("Это сообщение об ошибке.")
    warnings_errors_logger.critical("Это критическое сообщение.")

if __name__ == "__main__":
    log_messages()