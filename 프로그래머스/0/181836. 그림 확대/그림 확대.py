def solution(picture, k):
    answer = []
    
    for line in picture:
        expanded = ""
        for i in line:
            expanded += i * k
        for j in range(k):
            answer.append(expanded)
    return answer