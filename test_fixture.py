from unittest.mock import patch

import pytest


class Fruit:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name


class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author

'''
@patch.multiple('backend.libs.reference.ServiceReferenceModule',
                get_countries=MagicMock(return_value=COUNTRIES_MOCK_RESPONSE),
                get_regions=MagicMock(return_value=REGIONS_MOCK_RESPONSE))
                '''

@pytest.fixture
def my_fruit():
    return Fruit("apple")


@pytest.fixture
def fruit_basket(my_fruit):
    return [Fruit("banana"), my_fruit]


@pytest.fixture
def db_fixture():
    return [Book('Art of', 'James'), Book('Clear Code', 'Pablo')]


def test_my_fruit_in_basket(my_fruit, fruit_basket):
    assert my_fruit in fruit_basket


def test_bool_model(db_fixture):
    assert db_fixture[0].author == 'James'