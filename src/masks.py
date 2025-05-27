def get_mask_card_number(card_number: str) -> str:
    """Функция, которая принимает на вход номер карты и возвращает её маску"""
    new_mask_card = card_number[:4] + " " + card_number[4:6] + " **" + " " + card_number[-4:]
    return new_mask_card


def get_mask_account(card_number: str) -> str:
    """Функция, которая принимает на вход номер счёта и возвращает его маску"""
    return f"**{card_number[-4:]}"
