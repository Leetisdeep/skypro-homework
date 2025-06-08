import os
from typing import Dict

import requests


def convert_currency(transaction: Dict) -> float:
    amount = transaction.get("amount", 0)
    currency = transaction.get("currency", "RUB")

    if currency == "RUB":
        return float(amount)

    api_key = os.getenv("API_KEY")
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"

    headers = {"apikey": api_key}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        result = response.json()
        return float(result["result"])
    else:
        return 0.0
