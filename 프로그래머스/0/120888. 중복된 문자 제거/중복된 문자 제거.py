def solution(my_string):
    answer = ''
    for i in my_string: # people들이 하나씩 i로 들러감
        if i not in answer: #근데 answer에 i가 없으면
            answer += i # answer에 i를 저장
    return answer #그래서 겹치는 애들이 하나씩 빠지는구나 peol