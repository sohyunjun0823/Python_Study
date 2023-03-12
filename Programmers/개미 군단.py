def solution(hp):
    answer = 0
    # 장군개미의 수 = a, 병정개미의 수 = b, 일개미의 수 = c
    a = hp // 5
    t = hp - a * 5
    if  t > 3:
        b = t // 3
    elif t == 3:
        b = t // 3
    elif t < 3:
        b = 0
    if t >= 3:
        c = t - b * 3
    elif t < 3:
        c = t
    answer = a + b + c
    return answer
