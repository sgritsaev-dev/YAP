import datetime
from decimal import Decimal
import re

goods = {'Морковь': [  # Продукт "Морковь" покупали дважды:
        {'amount': Decimal('2'), 'expiration_date': datetime.date(2024, 1, 1)},
        {'amount': Decimal('3'), 'expiration_date': datetime.date(2024, 4, 2)}],
    'Пельмени Универсальные': [
        {'amount': Decimal(
            '0.5'), 'expiration_date': datetime.date(2024, 2, 15)},
        {'amount': Decimal('2'), 'expiration_date': datetime.date(2024, 2, 1)}
],
    'Вода': [{'amount': Decimal('1.5'), 'expiration_date': None}],
    'ВоДица': [{'amount': Decimal('1.5'), 'expiration_date': None}]
}


def add(items, title, amount, expiration_date=None):
    if expiration_date:
        exp_date = datetime.datetime.strptime(expiration_date, '%Y-%m-%d').date()
    else:
        exp_date = expiration_date
    if title in items:
        # Несмотря на то, что в задаче нет условия, когда добавляется продукт
        # той же даты, что уже есть в холодильнике, прописал его. Это логично,
        # что та же партия прибавится, а не задублируется.
        for el in items[title]:
            if el['expiration_date'] == exp_date:
                el['amount'] += amount
            else:
                items[title].append(
                    dict(
                        amount=amount,
                        expiration_date=exp_date))
                break
    else:
        items.setdefault(
            title,
            []).append(
            dict(
                amount=amount,
                expiration_date=exp_date))


def add_by_note(items, note):
    raw_data = note.split()
    try:
        datetime.datetime.strptime(raw_data[-1], '%Y-%m-%d')
        exp = raw_data[-1]
        ntamount = Decimal(raw_data[-2])
        title = ' '.join(el for el in raw_data[:-2])
    except:
        exp = None
        ntamount = Decimal(raw_data[-1])
        title = ' '.join(el for el in raw_data[:-1])
    add(items, title, ntamount, exp)


def find(items, needle):
    return [title for title in items.keys() if re.search(
        fr'\b.*{needle}.*\b', title, flags=re.IGNORECASE)]


def amount(items, needle):
    # Функция работает на основе функции find() - параметр needle будет
    # неисчерпывающим, то найдутся все соответствия. Также функция вернет
    # сумму по всем соответствиям. Например, если поиск будет по "д", а в
    # холодильнике будет "Вода" и "Водица" - функция вернет сумму обоих
    # продуктов.
    res = Decimal(0)
    for title in find(items, needle):
        for each in items[title]:
            res += each['amount']
    return res


def expire(items, in_advance_days=0):
    date_x = datetime.date.today() + datetime.timedelta(days=in_advance_days)
    stinky_goods = [(title, el['amount']) for title in items for el in items[title]
                    if el['expiration_date'] is not None and el['expiration_date'] <= date_x]
    res = {}
    for key, value in stinky_goods:
        res[key] = res.get(key, 0) + value
    return list(res.items())