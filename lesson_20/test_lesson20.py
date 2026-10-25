import json


def test_user_data():
    with open("test_data.json", "r", encoding="utf-8") as file:
        test_data = json.load(file)

    user = test_data["user"]

    assert user["name"] == "Maria"
    assert user["role"] == "tester"