from ..masks import masks_logger


def mask_card_number(card_number: str) -> str:
    masks_logger.debug(f"Маскирование номера карты: {card_number}")
    if len(card_number) != 16:
        masks_logger.error(f"Некорректная длина номера карты: {card_number}")
        raise ValueError("Номер карты должен содержать 16 цифр")
    masked_number = card_number[:4] + " **** **** " + card_number[-4:]
    masks_logger.info(f"Номер карты успешно замаскирован: {masked_number}")
    return masked_number
