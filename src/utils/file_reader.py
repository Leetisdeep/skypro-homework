import json
from typing import Dict, List

import pandas as pd


def read_transactions_from_csv(file_path: str) -> List[Dict]:
    """
    Считывает финансовые операции из CSV-файла.
    Args:
        file_path (str): Путь к CSV-файлу.
    Returns:
        List[Dict]: Список словарей с транзакциями.
    """
    try:
        df = pd.read_csv(file_path)
        return df.to_dict(orient="records")
    except Exception as e:
        raise ValueError(f"Ошибка при чтении CSV-файла: {e}")


def read_transactions_from_excel(file_path: str) -> List[Dict]:
    """
    Считывает финансовые операции из Excel-файла.
    Args:
        file_path (str): Путь к Excel-файлу.
    Returns:
        List[Dict]: Список словарей с транзакциями.
    """
    try:
        df = pd.read_excel(file_path)  # Changed from read_csv to read_excel
        return df.to_dict(orient="records")
    except Exception as e:
        raise ValueError(f"Ошибка при чтении Excel-файла: {e}")


def read_transactions_from_json(file_path: str) -> List[Dict]:
    """
    Считывает финансовые операции из JSON-файла.
    Args:
        file_path (str): Путь к JSON-файлу.
    Returns:
        List[Dict]: Список словарей с транзакциями.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)
