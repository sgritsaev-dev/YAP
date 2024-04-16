from math import sqrt
from typing import Optional, Union

# pep8-naming: проверяет именование классов, функций и переменных в
# соответствии с PEP 8;
# flake8-isort: проверяет корректность последовательности импортов


def add_numbers(first: int, second: int) -> int:
    return first + second


def calculate_square_root(number: Union[float, int]) -> float:
    return sqrt(number)


def calc(your_number: Union[int, float]) -> Optional[str]:
    if your_number <= 0:
        return None
    root = calculate_square_root(your_number)
    return ('Мы вычислили квадратный корень из введённого вами числа. '
            f'Это будет: {root}')


first: int = 10
second: int = 5

print('Сумма чисел: ', add_numbers(first, second))

print(calc(25.5))
