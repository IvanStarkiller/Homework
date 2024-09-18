from datetime import datetime
from typing import Union

from src.masks import get_mask_card_number


def mask_account_card(card: str) -> str:
    """Функция работает и с картой и со счетом"""
    card_number = "".join(i if i.isdigit() else "" for i in card)
    number_card_mask = get_mask_card_number(card_number)
    card_name = "".join("" if i.isdigit() else i for i in card)
    card_mask = card_name + number_card_mask
    return card_mask


print(mask_account_card("Visa Platinum 7000792289606364"))


def get_date(user_date: Union[str]) -> str:
    """Функция получения даты в определенном формате и возвращения в формате ДД.ММ.ГГГГ"""
    date_format = datetime.strptime(user_date, "%Y-%m-%dT%H:%M:%S.%f")
    new_date = date_format.strftime("%d.%m.%Y")
    return new_date
