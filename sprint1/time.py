# Получаем данные в секундах
response = 424562

# Переведите полученное значение в необходимые единицы измерения
days = response//86400
hours = (response//3600)%24
minutes = (response//60)%60
seconds = response%60

print(response, 'секунд - это')
print('Дней:', days)
print('Часов:', hours)
print('Минут:', minutes)
print('Секунд:', seconds)

# 424562 секунд - это
# Дней: 4
# Часов: 21
# Минут: 56
# Секунд: 2
