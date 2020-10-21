"""
Закодируй число

Чип и Дейл устали от публичности. Чтобы как-то обезопасить свои
персональные данные, они решили шифровать sms - сообщения. Числа
они решили разворачивать. Помогите им написать программу для
кодирования чисел.

Формат ввода
На вход подается целое число n, по модулю не превосходящее 10000.

Формат вывода
На выходе должно быть число, развернутое в обратном порядке.

Пример 1
Ввод
123

Вывод
321

Пример 2
Ввод
-150

Вывод
-51
"""


def encode_number(number: int) -> int:
    if number == 0:
        return 0

    result: list = []

    if number < 0:
        result.append('-')

    result.extend([digit for digit in str(abs(number))[::-1]])

    return int(''.join(result))


number_for_encoding = int(input())

print(encode_number(number=number_for_encoding))
