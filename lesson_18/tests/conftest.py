import pytest
from lesson_18.api.booking_api import BookingAPI


@pytest.fixture()
def client():
    """Создает объект класса BookingAPI"""

    return BookingAPI()


@pytest.fixture()
def booking_id(client):
    """Достает id созданного клиента"""

    response = client.create_booking()
    return response.json()["bookingid"]