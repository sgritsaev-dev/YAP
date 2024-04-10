# Количество корзин с овощами, шт.
baskets = 462 
# Средний вес овощей в одной корзине, кг.
average_weight = 25
# Стоимость одного килограмма урожая, в монетах.
price_per_kg = 175 


# Допишите функцию, которая рассчитывает вес и стоимость урожая.
def calc(amount, weight, price):
    total_weight = amount*weight
    total_price = total_weight*price
    return total_weight, total_price

# Вызовите функцию calc() и обработайте вернувшееся значение.
tw, tp = calc(baskets, average_weight, price_per_kg)
# Составьте f-строку и напечатайте её.
print(f'Общий вес урожая: {tw} кг. Оценённая стоимость урожая: {tp}.')