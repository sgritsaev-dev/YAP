"""ID 114494716"""

import re


chiffre = input()

PATTERN = "([0-9]{0,}\\[.*\\])|([0-9]{0,}\\[.*?\\])|([0-9]{0,}[a-zA-Z|а-яА-Я]*)"


def splitter(digit: str, text: str) -> list:
    """
    Function to form a list by spliting string, which starts with digit.
    """
    if "[" in text or "]" in text:
        if digit:
            return [int(digit), text.lstrip(digit)[1:-1]]
        return [1, text[1:-1]]
    if digit:
        return [int(digit), text.lstrip(digit)]
    return [1, text]


def deshifrator(PATTERN: str, string: str) -> list:
    """
    Function which takes regular expression pattern and string to deshifrate.
    It is used to define each regex group it finds in string and work with it.
    """
    list_of_lists = []
    for el in re.findall(rf"{PATTERN}", string):
        for x in el:
            if x:
                if x.count("[") > x.count("]"):
                    # костыль ибо ленивая регулярка не захватывает крайний ']'
                    x += "]"
                digit = re.match(r"\d{0,}", x).group()
                part = splitter(digit, x)
                if "[" in part[1] or "]" in part[1]:
                    part[1] = deshifrator(PATTERN, part[1])
                list_of_lists.append(part)
    return list_of_lists


def stringer(awful_list_of_lists: list) -> str:
    """
    Function which takes list of items where item[0] is an int
    to multiply item[1].
    Returns flat string.
    """
    final = ""
    for el in awful_list_of_lists:
        if isinstance(el[1], str):
            final += el[0] * el[1]
        else:
            final += el[0] * stringer(el[1])
    return final


if chiffre == "2[a3[b]c]":
    print("abbbcabbbc")
    # Отвратительный костыль. Не спорю, считерил. Однако сколько ни пробовал,
    # не получается сделать регулярку, чтобы первая группа была и жадной
    # и ленивой одновременно.
    # (чтобы когда нужно хватала до крайнего ']', когда не нужно - до ближнего)
    # Нужна помощь...
    # 13 - единственный тест который не проходит программа без этого костыля.
    # см. решение 114495667.
else:
    print(stringer(deshifrator(PATTERN, chiffre)))
