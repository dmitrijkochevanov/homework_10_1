import pytest


@pytest.fixture
def mask_account_card():
    return "Счет 64686473678894779589"


@pytest.fixture
def new_date():
    return "2018-07-11T02:26:18.671407"


@pytest.fixture
def mask_card():
    return "7000792289606361"


@pytest.fixture
def mask_account():
    return "73654108430135874305"


@pytest.fixture
def dictionary_key():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    ]


@pytest.fixture
def date_sorted():
    return [
        {'id': '41428829', 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': '939719570', 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    ]
