from random import randint

# Начальная температура чая
current_temperature = 85

while current_temperature>60:
    minus = randint(1,3)
    current_temperature-=minus
    print(f'''Прошла минута.
Чай остыл ещё на {minus} °C. Текущая температура: {current_temperature} °C''')
print('Время пить чай!')
# Объявите цикл while
# В теле цикла получите случайное значение температуры, 
# на которое остыл чай в этой итерации (в диапазоне от 1 до 3).
# Уменьшите температуру чая на полученное значение.
# Напечатайте нужные сообщения.

# Напечатайте сообщение, которое должно быть выведено после завершения цикла.