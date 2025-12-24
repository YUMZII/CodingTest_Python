def solution(strArr):
    count = {}

    for s in strArr:
        length = len(s)
        if length in count:
            count[length] += 1
        else:
            count[length] = 1

    return max(count.values())
