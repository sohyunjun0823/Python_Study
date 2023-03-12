def solution(my_string):
    answer = 0
    number_string = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in my_string:
        if i in number_string:
            answer = answer + int(i)
        
    return answer
