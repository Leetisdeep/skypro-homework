from datetime import datetime


def mask_account_number(account_number: str) -> str:
    """
    Маскирует номер счёта.
    По условию тестов нужно выводить '**' + последние 4 символа,
    а если длина номера меньше 4, то '**' + сам номер.
    """
    account_number = account_number.strip()
    if not account_number:
        return ""
    if len(account_number) < 4:
        return "**" + account_number
    return "**" + account_number[-4:]


def mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты.
    Из примеров видно, что шаблон для маски выглядит так:
      - первые 4 цифры,
      - пробел,
      - следующие 2 цифры,
      - '**',
      - пробел,
      - '****',
      - пробел,
      - последние 4 цифры.
    Пример: 1234567890123456 -> 1234 56 ** 3456
    """
    card_number = card_number.strip()
    if not card_number:
        return ""

    # Для упрощения считаем, что карта >= 8 символов (как в тестах).
    # Если меньше, вернём как есть — или можно придумать собственное правило маскировки.
    if len(card_number) < 8:
        return card_number

    return f"{card_number[:4]} {card_number[4:6]} ** {card_number[-4:]}"


def mask_account_card(input_data: str) -> str:
    """
    Определяет, с чем мы имеем дело — счёт или карту — и маскирует соответствующим образом.
    Если строка пуста или содержит только пробелы, возвращаем пустую строку.
    Если из строки невозможно вытащить номер, возвращаем без изменений.
    """
    input_data = input_data.strip()
    if not input_data:
        return ""

    # Проверяем, начинается ли строка со слова "Счет "
    if input_data.startswith("Счет "):
        # Все, что после "Счет " - номер счёта
        account_number = input_data[len("Счет ") :].strip()
        return "Счет " + mask_account_number(account_number)
    else:
        # Предполагаем, что это карта (либо что-то, что по тестам маскируется как карта)
        # Разделим строку, чтобы отделить тип карты (или другое слово) от номера.
        # Обычно номер карты идёт последним "словом".
        parts = input_data.rsplit(" ", 1)
        if len(parts) < 2:
            # Нет явно выделенного номера в конце — возвращаем как есть.
            return input_data
        card_type, number = parts
        return card_type + " " + mask_card_number(number)


def get_date(date_str: str) -> str:
    """
    Парсит строку даты формата YYYY-MM-DDTHH:MM:SS
    и возвращает её в формате DD.MM.YYYY.
    При несоответствии формату генерирует ValueError.
    """
    try:
        dt = datetime.strptime(date_str.strip(), "%Y-%m-%dT%H:%M:%S")
    except ValueError:
        raise ValueError(f"Invalid date format: {date_str}")
    return dt.strftime("%d.%m.%Y")
