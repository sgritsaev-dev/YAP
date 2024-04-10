from math import factorial as fact
from random import randint as rnd
value = rnd(1,10)
result = fact(value)
print(f'Факториал {value} равен {result}')