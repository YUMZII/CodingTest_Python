def solution(rank, attendance):
    answer = []
    
    for i in range(len(rank)):
        if attendance[i] == True:
            answer.append((rank[i], i))
    answer.sort()
    a=answer[0][1]
    b=answer[1][1]
    c=answer[2][1]
    
    return 10000 * a + 100 * b + c