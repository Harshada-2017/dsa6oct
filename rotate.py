
def solve(arr):
    if len(arr) == 0:
        return arr

    last = arr[len(arr) - 1]
    i = len(arr) - 1

    while i > 0:
        arr[i] = arr[i - 1]
        i = i - 1

    arr[0] = last

    return arr
