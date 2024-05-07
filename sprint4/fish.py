n = int(input())
lst = [int(el) for el in input().split()]
ls = set(lst)
total = int(input())
def checker(n, lst, total):
    for el in lst:
        if el in ls:
            ls.remove(el)
        if (total-el) in ls:
            return f'{el} {(total-el)}'
    return None
print(checker(n, lst, total))










