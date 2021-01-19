import random

# The construction of the method random.random() числа с плавающей точкой в диапазоне [0, 1).
#
# The function generate a random float number.
#
# Методы, которые используются с random-классом являются связанными методами скрытых экземпляров.
# Экземпляры класса Random можно использовать в многопоточных программах, в которых для каждого потока создается
# отдельный экземпляр.
print(random.random())

# The method select and determine numbers in a range of (a, b)
# It return random elements from the selected and don't create any range object.
print(random.randrange(0, 1000))

# Метод выбирает и определяет числа с плавающей точкой в диапазоне [a, b).
# Возвращает число с плавающей точкой из заданной области;
print(random.uniform(0, 1000))

# Используется для нормального распределения, где mean – это мю,
# а sdev – это сигма, которые используются при нормальном распределении;
print(random.normalvariate(mu=0, sigma=1000))

# Класс Random используется для создания экземпляра, который независимые генераторы случайных чисел.
print(random.Random)
