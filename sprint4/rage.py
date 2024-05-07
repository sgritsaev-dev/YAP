n = int(input())
arr = list(map(int, input().strip().split()))
window_size = int(input())
def calc(arr, window_size):
    t = sum(arr[:window_size])
    res = [t / window_size]
    for i in range(window_size, len(arr)):
        t += arr[i] - arr[i - window_size]
        res.append(t / window_size)
    return res
print(*calc(arr, window_size))