import pytest

from src.masks import get_mask_card, get_mask_account
from .conftest import mask_card


def test_get_mask_card(mask_card):
    assert get_mask_card(mask_card) == "7000 79** **** 6361"


@pytest.mark.parametrize("number, mask_account",
    [
        ("73654108430135874305", "**4305"),
        ("64686473678894779589", "**9589"),
        ("35383033474447895560", "**5560"),
        ("73654108430135874305", "**4305"),
    ],
)
def test_get_mask_account(number, mask_account):
    assert get_mask_account(number) == mask_account
