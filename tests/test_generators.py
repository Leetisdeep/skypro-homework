# tests/test_generators.py
import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def sample_transactions():
    return [
        {"amount": 100.0, "currency": "USD", "description": "Payment #1"},
        {"amount": 150.0, "currency": "EUR", "description": "Payment #2"},
        {"amount": 70.0, "currency": "USD", "description": "Payment #3"},
    ]


def test_filter_by_currency_usd(sample_transactions):
    result = list(filter_by_currency(sample_transactions, "USD"))
    assert len(result) == 2
    for r in result:
        assert r["currency"] == "USD"


def test_filter_by_currency_eur(sample_transactions):
    result = list(filter_by_currency(sample_transactions, "EUR"))
    assert len(result) == 1
    for r in result:
        assert r["currency"] == "EUR"


def test_transaction_descriptions(sample_transactions):
    desc_gen = transaction_descriptions(sample_transactions)
    result = list(desc_gen)
    assert result == ["Payment #1", "Payment #2", "Payment #3"]


@pytest.mark.parametrize(
    "start,stop,expected",
    [
        (1, 1, ["0000 0000 0000 0001"]),
        (1, 2, ["0000 0000 0000 0001", "0000 0000 0000 0002"]),
    ],
)
def test_card_number_generator(start, stop, expected):
    cards = list(card_number_generator(start, stop))
    assert cards == expected
