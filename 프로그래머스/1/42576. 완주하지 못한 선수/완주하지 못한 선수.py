def solution(participant, completion):
    from collections import Counter
    p = Counter(participant)
    c = Counter(completion)
    answer = p - c
    return list(answer.keys())[0]
