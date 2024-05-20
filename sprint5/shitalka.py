n = int(input())
k = int(input())

# n=5
# k=2
ls = list(range(1, n+1))
# print(ls)
starting_point = -1
while len(ls) > 1:
    for i in range(k):
        starting_point += 1
        if starting_point == len(ls):
            starting_point = 0
    ls.pop(starting_point)
    starting_point -= 1
print(*ls)
