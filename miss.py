
def solve(arr):
    n = len(arr) + 1
    total = n * (n + 1) // 2
    s = 0

    for i in arr:
        s = s + i

    return total - s
