def solution(n):
    answer = 0
    for i in range (n):
        #print(i * i)
        #print(n)
        if n == i * i:
            answer = 1
            break
        else:
            answer = 2
    return answer
