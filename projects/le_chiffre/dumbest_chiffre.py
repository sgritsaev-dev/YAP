"""Омерзительнейшая задача, решение 114499757"""

RUSSIAN = "абвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
ENGLISH = "abcdefghijklmnopqrstuvwxyABCDEFGHIJKLMNOPQRSTUVWXY"

x = input()

# Потел 3 часа, пытался через regex решить - не вышло.
# В итоге сдаю вот такой кал(((

res = ""
if x[0] in ENGLISH or x[0] in RUSSIAN:
    res += '"' + x[0] + '"'
else:
    res += str(x[0])
for i in range(1, len(x)):
    if x[i] in ENGLISH or x[i] in RUSSIAN:
        if x[i - 1] in ENGLISH or x[i - 1] in RUSSIAN or x[i - 1] == "]":
            res += "+" + '"' + x[i] + '"'
        elif x[i - 1].isdigit():
            res += "*" + '"' + x[i] + '"'
        else:
            res += '"' + x[i] + '"'
    elif x[i].isdigit():
        if x[i - 1] in ENGLISH or x[i - 1] in RUSSIAN or x[i - 1] == "]":
            res += "+" + x[i]
        elif x[i - 1].isdigit():
            res += x[i]
        else:
            res += x[i]
    elif x[i] == "[":
        if x[i - 1] in ENGLISH or x[i - 1] in RUSSIAN or x[i - 1] == "]":
            res += "+" + "("
        elif x[i - 1].isdigit():
            res += "*" + "("
        else:
            res += "("
    elif x[i] == "]":
        res += ")"

print(eval(res))
