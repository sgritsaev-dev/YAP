sequence_1 = [69, 59, 57, 60, 63, 44, 46, 69]
sequence_2 = [33, 73, 50, 25, 36, 68, 52, 76]

def compare_sequences(lst1, lst2):
    if lst1==lst2:
        return f'Списки равны.'
    elif lst1>lst2:
        return f'Список {lst1} больше.'
    else:
        return f'Список {lst2} больше.'

# Вызовите функцию compare_sequences(),
# передайте в неё списки sequence_1 и sequence_2.
# Напечатайте результат, который вернёт функция.
res = compare_sequences(sequence_1, sequence_2)
print(res)