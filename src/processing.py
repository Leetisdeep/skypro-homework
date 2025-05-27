def filter_by_state(info: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция, которая возвращает новый список словарей, содержащий только те словари, у которых ключ 'state'
    соответствует указанному значению."""
    result = []
    for i in info:
        if i.get("state") == state:
            result.append(i)
    return result


def sort_by_date(info: list[dict], reverse=False) -> list[dict]:
    """Функция должна возвращать новый список, отсортированный по дате"""
    return sorted(info, key=lambda x: x["date"], reverse=reverse)
