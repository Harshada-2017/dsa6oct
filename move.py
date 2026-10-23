
def solve(arr):
    result = []
    count = 0

    for i in arr:
        if i != 0:
            result.append(i)
        else:
            count = count + 1

    while count > 0:
        result.append(0)
        count = count - 1

    return result
