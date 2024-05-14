def count_less(list_of_numbers):
    print(*list(map(lambda x: sorted(list_of_numbers, key=int).index(x), list_of_numbers)))

count_less(input().split())