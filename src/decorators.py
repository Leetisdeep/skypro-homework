# decorators.py
import functools
import logging
import sys
from datetime import datetime
from typing import Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор, логирующий работу функции.
    Если filename передан, логи записываются в файл с указанным именем.
    Иначе — выводятся в консоль.

    :param filename: Имя файла для записи логов (необязательно).
    :return: Функция-декоратор.
    """

    # Создаём функцию-декоратор
    def decorator(func: Callable) -> Callable:

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            """
            Обёртка, которая логирует вызов функции, её результат или возникшую ошибку.
            """
            # Конфигурация логгера для каждого вызова декоратора
            logger = logging.getLogger(func.__name__)
            logger.setLevel(logging.INFO)

            # Если filename передан, пишем в файл; иначе — в консоль
            if filename:
                handler = logging.FileHandler(filename, mode="a", encoding="utf-8")
            else:
                handler = logging.StreamHandler(sys.stdout)

            # Чтобы не дублировать логи при многократных вызовах
            logger.handlers = []
            logger.addHandler(handler)

            log_msg_start = (
                f"[{datetime.now().isoformat()}] "
                f"Start function '{func.__name__}' with args={args}, kwargs={kwargs}"
            )
            logger.info(log_msg_start)

            try:
                result = func(*args, **kwargs)
                log_msg_success = f"[{datetime.now().isoformat()}] " f"Function '{func.__name__}' returned {result!r}"
                logger.info(log_msg_success)
            except Exception as e:
                log_msg_error = (
                    f"[{datetime.now().isoformat()}] "
                    f"Error in function '{func.__name__}': {type(e).__name__}. "
                    f"Args were {args}, kwargs were {kwargs}. "
                    f"Exception message: {str(e)}"
                )
                logger.error(log_msg_error)
                # Можно пробросить исключение дальше, чтобы не "глотать" ошибку
                raise

            # Важно закрыть handler, чтобы освободить ресурсы (особенно в случае логирования в файл)
            handler.close()
            logger.removeHandler(handler)

            return result

        return wrapper

    return decorator
