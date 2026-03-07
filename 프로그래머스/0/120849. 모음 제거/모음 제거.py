def solution(my_string):
    answer = ''
    all = ("a,e,i,o,u")
    for i in my_string:
        if i not in all:
            answer += i
    return answer