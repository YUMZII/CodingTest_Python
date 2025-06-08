def solution(num_list):
    add = 0
    multiply = 1
    answer = 0
    
    for i in num_list:
        multiply *= i
        add += i
    answer = 1 if multiply < add * add else 0
    return answer 