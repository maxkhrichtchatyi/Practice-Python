class TestFactorize(unittest.TestCase):
    def test_wrong_types_raise_exception(self) -> None:
        """
        Проверяет, что передаваемый в функцию аргумент типа
        float или str вызывает исключение TypeError.
        """
        cases = ('string', 1.5)
        for x in cases:
            with self.subTest(x=x):
                self.assertRaises(TypeError, factorize, x)

    def test_negative(self) -> None:
        """
        Проверяет, что передача в функцию factorize отрицательного
        числа вызывает исключение ValueError.
        """
        cases = (-1, -10, -100)
        for x in cases:
            with self.subTest(x=x):
                self.assertRaises(ValueError, factorize, x)

    def test_zero_and_one_cases(self) -> None:
        """
        Проверяет, что при передаче в функцию целых чисел 0 и 1,
        возвращаются соответственно кортежи (0,) и (1,).
        """
        cases = (0, 1)
        for x in cases:
            with self.subTest(x=x):
                self.assertEqual(factorize(x), (x,))

    def test_simple_numbers(self) -> None:
        """
        Проверяет, что для простых чисел возвращается кортеж,
        содержащий одно данное число.
        """
        cases = (3, 13, 29)
        for x in cases:
            with self.subTest(x=x):
                self.assertEqual(factorize(x), (x,))

    def test_two_simple_multipliers(self) -> None:
        """
        Проверяет случаи, когда передаются числа для которых функция
        factorize возвращает кортеж с числом элементов равным 2.
        """
        cases = (
            (6, (2, 3)),
            (26, (2, 13)),
            (121, (11, 11))
        )
        for x, value in cases:
            with self.subTest(x=x):
                self.assertEqual(factorize(x), value)

    def test_many_multipliers(self) -> None:
        """
        Проверяет случаи, когда передаются числа для которых функция
        factorize возвращает кортеж с числом элементов больше 2.
        """
        cases = (
            (1001, (7, 11, 13)),
            (9699690, (2, 3, 5, 7, 11, 13, 17, 19))
        )
        for x, value in cases:
            with self.subTest(x=x):
                self.assertEqual(factorize(x), value)
