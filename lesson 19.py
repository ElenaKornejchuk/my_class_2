# if 10 > 5:
#     print("Условие выполнено")


# def calculate_average(a, b):
#     return (a + b) / 2
#
# print(calculate_average(10, 20))

#
# price = 500
# quantity = 0
#
# print(price / quantity)


# products = ["ноутбук", "мышь", "клавиатура"]
#
# # print(products[10])
#
# print(int("ноутбук"))

# def is_adult(age):
#     return age >= 18
#
# print(is_adult("ghj"))

# def is_adult(age):
#     if not isinstance(age, int):
#         raise TypeError("Возраст должен быть целым числом")
#
#     if age < 0 or age > 120:
#         raise ValueError(f"Возраст должен быть от 0 до 120, получено: {age}"
# )
#
#     return age >= 18
#
# print(is_adult(300))

# class AgeError(Exception):
#     pass
# #
# def is_adult(age):
#     if not isinstance(age, int):
#         raise TypeError("Возраст должен быть целым числом")
#
#     if age < 0 or age > 120:
#             raise AgeError("Указан недопустимый возраст")
#
#     return age >= 18
#
# print(is_adult(300))

# products = ["телефон", "планшет", "ноутбук"]
#
# try:
#     print(products[1])
# except IndexError:
#     print("Товар с таким номером не найден")
#
# print("Программа продолжает работу")

# user_input = "abc"
#
# try:
#     number = int(user_input)
# except (ValueError, TypeError):
#     print("Не удалось преобразовать значение в число")
#
#
# try:
#     number = int(user_input)
# except ValueError:
#     print("Передано некорректное значение")
# except TypeError:
#     print("Передан объект неподходящего типа")


try:
    result = 100 / 0
except ZeroDivisionError:
    print("На ноль делить нельзя")
else:
    print(f"Результат: {result}")
finally:
    print("Вычисление завершено")


















