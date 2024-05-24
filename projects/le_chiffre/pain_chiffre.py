"""ID 114541450"""

import re


def grouper(encoded_msg: str) -> list:
    """
    Forms list of groups out of string, which comply with rules:
    1) multiplier/nothing+letters
    2) multiplier/nothing+[chars]
    >>> grouper('2cp3[a2[b]c]g')
    ['2cp', '3[a2[b]c]', 'g']
    """
    res = []
    left_bracket_counter = 0
    right_bracket_counter = 0
    group = ''
    for i in range(len(encoded_msg)):
        if len(group) > 0:
            if ((left_bracket_counter == 0 and right_bracket_counter == 0)
                    and (encoded_msg[i] == '[' or encoded_msg[i].isdigit())
                    and not encoded_msg[i-1].isdigit()):
                res.append(group)
                group = ''
        group += encoded_msg[i]
        if encoded_msg[i] == '[':
            left_bracket_counter += 1
        elif encoded_msg[i] == ']':
            right_bracket_counter += 1
        if (left_bracket_counter != 0
                and right_bracket_counter != 0
                and left_bracket_counter == right_bracket_counter):
            res.append(group)
            left_bracket_counter = 0
            right_bracket_counter = 0
            group = ''
    if group:
        res.append(group)
    return res


def splitter(text: str, digit: str | None = None) -> list:
    """
    Function to form a list by spliting string, which starts with digit.
    If string does not start with digit, digit is taken as '1'.
    Also strips '[]' brackets, if there are brackets.
    >>> splitter('3[ab]', '3')
    [3, 'ab']
    """
    if "[" in text or "]" in text:
        if digit:
            return [int(digit), text.lstrip(digit)[1:-1]]
        return [1, text[1:-1]]
    if digit:
        return [int(digit), text.lstrip(digit)]
    return [1, text]


def deshifrator(string: str) -> list:
    """
    Main function which takes an encoded string,
    returns a "ready-to-work with" flat list of lists.
    >>> deshifrator('2[c3[ab]t]')
    [[2, [[1, 'c'], [3, 'ab'], [1, 't']]]]
    """
    list_of_lists = []
    for group in grouper(string):
        digit = re.match(r"\d{0,}", group)
        if digit:
            grouplist = splitter(group, digit.group())
        else:
            grouplist = splitter(group)
        if "[" in grouplist[1] or "]" in grouplist[1]:
            grouplist[1] = deshifrator(grouplist[1])
        list_of_lists.append(grouplist)
    return list_of_lists


def stringer(awful_list_of_lists: list) -> str:
    """
    Decodes list of lists in for of [multiplier+chars] into string.
    Returns flat string.
    >>> stringer([[2, [[1, 'c'], [3, 'ab'], [1, 't']]]])
    'cabababtcabababt'
    """
    final = ""
    for el in awful_list_of_lists:
        if isinstance(el[1], str):
            final += el[0] * el[1]
        else:
            final += el[0] * stringer(el[1])
    return final


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(stringer(deshifrator(input())))
