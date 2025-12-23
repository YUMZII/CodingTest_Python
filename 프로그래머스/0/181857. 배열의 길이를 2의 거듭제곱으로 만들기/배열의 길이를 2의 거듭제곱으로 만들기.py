def solution(arr):
    s = 1
    while s < len(arr):
        s *= 2
    n = s - len(arr)
    arr += [0] * n
    return arr