from src.masks import get_mask_account,get_mask_card
def get_mask_account_card(number: str) -> str:
    """Функция принимает строку и выдает замаскированный
    номер карты или счета"""
    if len(number.split()[-1]) == 16:
        mask_card = get_mask_card(number.split()[-1])
        result = f"{number[:-16]}{mask_card}"
        return result
    elif len(number.split()[-1]) == 20:
        mask_account = get_mask_account(number.split()[-1])
        result = f"{number[:-20]}{mask_account}"
        return result

