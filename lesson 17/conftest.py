import pytest

from library import Library


# @pytest.ini.fixture
# def library():
#
#     librari = Library()
#
#     return librari

@pytest.fixture
def library():

    library = Library()

    yield library

    library.clear()