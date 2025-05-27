from src.utils.operation_counter import operation_counter
from src.utils.operation_search import operation_search


def test_search_operations_by_description():
    operations = [
        {"description": "Перевод с карты на карту"},
        {"description": "Открытие вклада"},
        {"description": "Перевод организации"},
    ]
    result = operation_search(operations, "перевод")
    assert len(result) == 2
    assert result[0]["description"] == "Перевод с карты на карту"
    assert result[1]["description"] == "Перевод организации"


def test_count_operations_by_categories():
    operations = [
        {"description": "Перевод с карты на карту"},
        {"description": "Открытие вклада"},
        {"description": "Перевод организации"},
    ]
    categories = ["перевод", "вклад"]
    result = operation_counter(operations, categories)
    assert result["перевод"] == 2
    assert result["вклад"] == 1
