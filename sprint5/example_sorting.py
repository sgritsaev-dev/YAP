n = int(input())
unsorted = input().split()
uns_copy = unsorted[:]
k = int(input())
example = input().split()

ex_res = dict()

for el in example:
    ex_res.setdefault(el, []).extend([el] * unsorted.count(el))
    while el in uns_copy:
        uns_copy.remove(el)
uns_copy.sort(key=int)
# print(ex_res)
res = []
for el in ex_res.values():
    res.extend(el)

print(*(res + uns_copy))
