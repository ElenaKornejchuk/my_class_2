# .txt — обычный текст.
#
# .json — структурированные
# данные, например словари и списки.
#
# .csv — табличные данные.

# with open("notes.txt", "r", encoding="utf-8") as file:
#     content = file.read()
#
# print(content)

# with open("notes.txt", "w", encoding="utf-8") as file:
#     file.write("Новый текст")

# with open("notes.txt", "a", encoding="utf-8") as file:
#     file.write("\nНовый текст4")


# "r" — чтение.
#
# "w" — запись с заменой прежнего содержимого.
#
# "a" — добавление в конец файла.
#
# "r+" — чтение и запись без предварительной очистки файла.
#
# "w+" — чтение и запись, при открытии прежнее содержимое очищается.
#
# "rb" — чтение в бинарном режиме.
#
# "wb" — запись в бинарном режиме.
#
# file = open("notes.txt", "r", encoding="utf-8")
# content = file.read()
# file.close()
#
# print(content)


import json

user = {
    "name": "Мария",
    "age": 27,
    "is_active": True,
    "skills": ["Python", "pytest"]
}

# with open("file_json.json", "w", encoding="utf-8") as file:
#     json.dump(user, file, ensure_ascii=False, indent=4)

# with open("file_json.json", "r", encoding="utf-8") as file:
#     user_data = json.load(file)
#
# # print(user_data)
# print(user_data["name"])


# dump() — записывает объект в файл.
#
# dumps() — преобразует объект в JSON-строку.
#
# load() — читает JSON из файла.
#
# loads() — преобразует JSON-строку в Python-объект.

# user = {"name": "Мария", "age": 27, "bool": True}
#
# json_text = json.dumps(user, ensure_ascii=False)
# print(json_text)
#
# restored_user = json.loads(json_text)
# print(restored_user)
#
# import requests
#
# url = "https://example.com/api/users"
#
# user_data = {
#     "name": "Мария",
#     "role": "tester"
# }
#
# respons = requests.post(url, json=user_data)
#
# import csv
#
# users = [
#     ["Мария", 27, "tester"],
#     ["Иван", 31, "developer"]
# ]

# with open("users.csv", "w", encoding="utf-8", newline="") as file:
#     writer = csv.writer(file)
#
#     writer.writerow(["name", "age", "role"])
#     writer.writerows(users)

#
# with open("users.csv", "r", encoding="utf-8", newline="") as file:
#     reader = csv.reader(file)
#
#     for row in reader:
#         print(row)
# #
# with open("missing.txt", "r", encoding="utf-8") as file:
#     content = file.read()

# try:
#     with open("missing.txt", "r", encoding="utf-8") as file:
#         content = file.read()
#
# except FileNotFoundError:
#     print("Файл не найден")


try:
    with open("settings.json", "r", encoding="utf-8") as file:
        settings = json.load(file)
except FileNotFoundError:
    print("Файл настроек не найден")
except json.JSONDecodeError:
    print("В файле настроек некорректный JSON")