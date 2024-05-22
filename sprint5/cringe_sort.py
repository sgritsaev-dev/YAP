n = 8
unsorted = [int(el) for el in "3 1 0 2 6 5 4 7".split()]
maxval=unsorted[0]
counter=0
for i in range(len(unsorted)):
    try:
        maxval=max(unsorted[:i+1])
        if maxval==i:
            counter+=1
    except:
        pass
print(counter)