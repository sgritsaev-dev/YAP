import re

x = 'd'

digit = re.match(r'\d{0,}', x).group()
print(re.match(r'\d{0,}', x).group())

def splitter(digit, text:str):
    if  '[' in text or ']'in text:
        if digit:
            return int(digit), text.replace(digit, '')[1:-1]
        return 1, text[1:-1]
    if digit:
        return int(digit), text.replace(digit, '')
    return 1, text
    
print(splitter(re.match(r'\d{0,}', x).group(), x))