from src.masks import get_mask_account, get_mask_card


def get_mask_account_card(number: str) -> str:
    """Функция принимает строку и выдает замаскированный
    номер карты или счета"""
    if len(number.split()[-1]) == 16:
        mask_card = get_mask_card(number.split()[-1])
        result_mask_card = f"{number[:-16]}{mask_card}"
        return result_mask_card
    elif len(number.split()[-1]) == 20:
        mask_account = get_mask_account(number.split()[-1])
        result_mask_account = f"{number[:-20]}{mask_account}"
    return result_mask_account


def get_new_date(old_date: str) -> str:
    """Функция принимает строку с датой и преобразует ее в более
    читаемый вид"""
    date_slise = old_date[0:10].split("-")
    return ".".join(date_slise[::-1])
