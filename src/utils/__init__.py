import logging
from pathlib import Path

# Создаем папку logs, если её нет
logs_dir = Path("logs")
logs_dir.mkdir(exist_ok=True)

# Настройка логера для модуля utils
utils_logger = logging.getLogger("utils")
utils_logger.setLevel(logging.DEBUG)

# Создаем file handler
file_handler = logging.FileHandler("logs/utils.log", mode="w")
file_handler.setLevel(logging.DEBUG)

# Создаем форматтер
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

# Добавляем handler к логеру
utils_logger.addHandler(file_handler)
