import requests


class BookingAPI:
    BASE_URL = "https://restful-booker.herokuapp.com"

    BOOKING_URL = f"{BASE_URL}/booking"
    TOKEN_URL = f"{BASE_URL}/auth"


    def get_all_bookings(self):
        """Получить все бронирования"""

        return requests.get(self.BOOKING_URL)

    def get_booking_by_id(self, booking_id):
        """Получить бронирование по id"""

        return requests.get(f"{self.BOOKING_URL}/{booking_id}")

    def get_token(self):
        """Получить токен"""

        data = {
            "username": "admin",
            "password": "password123"
        }

        response = requests.post(self.TOKEN_URL, json=data)
        return response.json()["token"]

    def create_booking(self):
        """Создать бронирование"""

        data = {
            "firstname": "Alex",
            "lastname": "Petrov",
            "totalprice": 250,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2026-09-01",
                "checkout": "2026-09-10"
            },
            "additionalneeds": "Breakfast"
        }

        return requests.post(self.BOOKING_URL, json=data)

    def patch_booking(self, booking_id, data):
        """Изменить бронирование"""

        headers = {
            "Cookie": f"token={self.get_token()}"
        }

        return requests.patch(
            f"{self.BOOKING_URL}/{booking_id}",
            json=data,
            headers=headers
        )

    def update_booking(self, booking_id):
        """Обновить бронирование"""

        data = {
        "firstname" : "Ivan",
        "lastname" : "Ivanov",
        "totalprice" : 111,
        "depositpaid" : True,
        "bookingdates" : {
            "checkin" : "2018-01-01",
            "checkout" : "2019-01-01"
        },
        "additionalneeds" : "Breakfast"
    }

        headers = {
            "Cookie": f"token={self.get_token()}"
        }

        return requests.patch(
            f"{self.BOOKING_URL}/{booking_id}",
            json=data,
            headers=headers
        )

    def delete_booking(self, booking_id):
        """Удалить бронирование"""

        headers = {
            "Cookie": f"token={self.get_token()}"
        }

        return requests.delete(
            f"{self.BOOKING_URL}/{booking_id}",
            headers=headers
        )