def solution(my_string, num1, num2):
    answer = list(my_string)
    temp = answer[num1] # temp = 'e'
    answer[num1] = answer[num2] # my_string = 'hlllo'
    answer[num2] = temp # my_string = 'hlelo'
    answer = ''.join(answer)
    
    print(answer)

    return anㄴswer
