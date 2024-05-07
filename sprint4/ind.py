x = [int(el) for el in input().split()]
k = int(input())
def checker(x, k):
    try:
        return x.index(k)
    except:
        if max(x)<k:
            return len(x)
        elif min(x)>k:
            return 0
        else:
            res = min(list(filter(lambda x: x>0, list(map(lambda y: k-y, x)))))
            return list(map(lambda y: y-k, x)).index(res)
print(checker(x,k))