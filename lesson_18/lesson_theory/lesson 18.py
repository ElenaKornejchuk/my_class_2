# Основные методы
# GET → получить данные
# POST → создать
# PUT → полностью изменить
# PATCH → частично изменить
# DELETE → удалить
from http.client import responses
from pprint import pprint

# запрос будет выглядеть так
# url       http://exemple.com/file
# method    GET / POST / PUT / PATCH / DELETE
# headers   Content-Type
# body      Data

# Сервер возвращает:
#
# status_code 200 / 300 / 400 /500
# headers
# body

#https://restful-booker.herokuapp.com/apidoc/index.html
import requests

from pprint import pprint

# response = requests.get("https://restful-booker.herokuapp.com/booking")

# if response.status_code == 200:
#     pprint(response.json())

# print(response.status_code)
# pprint(response.json())

# print(response.headers)


# URL = "https://restful-booker.herokuapp.com/booking"
#
# # https://restful-booker.herokuapp.com/booking/:id
#
#
# def get_booking_by_id(id_):
#     response = requests.get(URL + f"/{id_}")
#
#     return response
#
# info_booking_person = get_booking_by_id(22)
#
# if info_booking_person.status_code == 200:
#     pprint(info_booking_person.json())


# https://restful-booker.herokuapp.com/auth

# curl -X POST \
#   https://restful-booker.herokuapp.com/auth \
#   -H 'Content-Type: application/json' \
#   -d '{
#     "username" : "admin",
#     "password" : "password123"
# }'

URL_FOR_TOKEN = "https://restful-booker.herokuapp.com/auth"

# def get_token():
#     info = {
#     "username" : "admin",
#     "password" : "password123"
#     }
#
#     response = requests.post(URL_FOR_TOKEN, json=info)
#
#     return response
#
# token = get_token()
#
# if token.status_code == 200:
#     print(token.json())

def get_token():
    info = {
    "username" : "admin",
    "password" : "password123"
    }

    response = requests.post(URL_FOR_TOKEN, json=info)

    return response.json()["token"]
#
# token = get_token()
# print(token)


URL = "https://restful-booker.herokuapp.com/booking"
#
# curl -X POST \
#   https://restful-booker.herokuapp.com/booking \
#   -H 'Content-Type: application/json' \
#   -d '{
#     "firstname" : "Jim",
#     "lastname" : "Brown",
#     "totalprice" : 111,
#     "depositpaid" : true,
#     "bookingdates" : {
#         "checkin" : "2018-01-01",
#         "checkout" : "2019-01-01"
#     },
#     "additionalneeds" : "Breakfast"
# }'
#
#
def get_booking_by_id(id_):
    response = requests.get(URL + f"/{id_}")

    return response
#
def create_boooking():
    info = {
        "firstname": "user_test2",
        "lastname" : "user_test2",
        "totalprice" : 1220,
        "depositpaid" : True,
        "bookingdates" : {
            "checkin" : "2026-08-08",
            "checkout" : "2026-09-09"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.post(URL, json=info)

    return response
#
# result = create_boooking()
#
# test_id_user = result.json()["bookingid"]
#
# # pprint(result.status_code)
# # pprint(result.json())
# # pprint(result.json()["bookingid"])
#
# user1 = get_booking_by_id(test_id_user)
#
# pprint(user1.json())


# URL = "https://restful-booker.herokuapp.com/booking"
#
# def path_booking(id_):
#     info = {
#     "firstname" : "James",
#     "lastname" : "Brown"
#     }
#
#     headers = {
#         "Cookie": f"token={get_token()}"
#     }
#     response = requests.patch(URL + f"/{id_}", json=info, headers=headers)
#
#     return response
#
# result = create_boooking()
# test_id_user = result.json()["bookingid"]
#
# path_booking(test_id_user)
#
# response = get_booking_by_id(test_id_user)
# print(response.status_code)
# # print(response.text)
#
# pprint(response.json())










