def solution(myString):
    answer = []
    for i in list(myString.split('x')):
        if i !="":
            answer.append(i)
    return sorted(answer)