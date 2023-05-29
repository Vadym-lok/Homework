# from typing import Any
#
#
# def gets_a_number_joke(users_numbers: Any) -> str:
#     if users_numbers == 1:
#         return 'анекдот про школу'
#     elif users_numbers == 2:
#         return 'анекдот про рибака'
#     else:
#         return 'анекдот про кота'
#
# users_numbers = input('enter a number: ')
# print(gets_a_number_joke(users_numbers))


# def length_and_width_of_the_rectangle(length_rectangle: int | float, width_rectangle: int | float) -> float:
#     perimeter = length_rectangle + width_rectangle
#     return float(perimeter)
#
#
# length_rectangle = int(input())
# width_rectangle = int(input())
# print(length_and_width_of_the_rectangle(length_rectangle, width_rectangle))
# clearing_letters = ''
#
#
# def string_replace(string: str) -> str:
#     clearing_letters = string.replace('ї', '').replace('ж', '')
#
#     return clearing_letters
#
#
# string = input().lower()
# print(string_replace(string))
# clearing_letters = ''
#
#
# def string_replace(string: str, string_2: str) -> str:
#     for value in string_2:
#         string = string.replace(value.lower(), '')
#         string = string.replace(value.upper(), '')
#     return string
#
#
# string = 'хижак'
# string_2 = 'вікно'
# print(string_replace(string, string_2))
