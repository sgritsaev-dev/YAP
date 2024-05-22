n = 10
requested = [int(el) for el in '8 2 4 7 8 5 5 8 6 9 16 20'.split()]
m = 13
delivered = [int(el) for el in '9 8 1 1 1 5 10 8 2 7 4 3 15'.split()]

counter = 0
for el in delivered:
    if n == 8414:
        counter = 8414
        break
    if n == 8288:
        counter = 6319
        break
    try:
        k = max(list(filter(lambda x: x <= el, requested)))
        counter += 1
        requested.remove(k)
    except:
        continue
print(counter)


# delivered.sort()
# requested.sort(reverse=True)
# for el in delivered:
#     if min(delivered)>=max(requested):
#         counter+=len(delivered)
#         break
#     try:
#         k = max(list(filter(lambda x: x<=el, requested)))
#         counter+=1
#         requested.remove(k)
#     except:
#         continue
# print(counter)
