import logging
from pathlib import Path

logs_dir = Path("logs")
logs_dir.mkdir(exist_ok=True)


masks_logger = logging.getLogger("masks")
masks_logger.setLevel(logging.DEBUG)


file_handler = logging.FileHandler("logs/masks.log", mode="w")
file_handler.setLevel(logging.DEBUG)


file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

masks_logger.addHandler(file_handler)


def get_mask_card_number():
    return None


def get_mask_account():
    return None
