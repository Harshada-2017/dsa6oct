
def solve(arr):
    result = []

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                if arr[i] not in result:
                    result.append(arr[i])

    return result
