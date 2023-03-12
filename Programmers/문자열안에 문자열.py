def solution(str1, str2):
    answer = 2
    for i in range(len(str1)):
        sub_string = str1[i:i + len(str2)]
        if sub_string == str2:
            return 1
    return answer
