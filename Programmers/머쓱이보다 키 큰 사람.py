def solution(array, height):
    answer = 0
    for i in array:
        if i > height:
            answer = answer + 1
            print(answer)
        else:
            sum = 0
    return answer
