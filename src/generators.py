# src/generators.py
from collections.abc import Generator, Iterable
from typing import Any, Dict


def filter_by_currency(transactions: List[Dict], currency: str, json: bool = True) -> Iterator[Dict]:
    """
    Возвращает итератор по транзакциям, у которых валюта совпадает с переданной.
    """
    for tx in transactions:
        if json:
            if tx.get("operationAmount").get("currency").get("code") == currency:
                yield tx
        else:
            if tx.get("currency_code") == currency:
                yield tx


def transaction_descriptions(
    transactions: Iterable[Dict[str, Any]],
) -> Generator[str, None, None]:
    """
    Yield the ``description`` of each transaction (if present).
    """
    for txn in transactions:
        if isinstance(txn, dict) and "description" in txn:
            yield txn["description"]


def card_number_generator(start: int, stop: int) -> Generator[str, None, None]:
    """
    Yield zero-padded, 16-digit card numbers grouped as
    ``0000 0000 0000 0001`` … up to *stop* (inclusive).

    Raises
    ------
    ValueError
        If *start* is greater than *stop*.
    """
    if start > stop:
        raise ValueError("start must be &le; stop")

    for number in range(start, stop + 1):
        s = f"{number:016d}"  # 16-digit zero-padded string
        yield f"{s[:4]} {s[4:8]} {s[8:12]} {s[12:]}"
