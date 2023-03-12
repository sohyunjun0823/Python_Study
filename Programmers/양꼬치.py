def solution(n, k):
    answer = 0
    if n >= 10:
        answer = 12000 * n + 2000 * k - (n // 10) * 2000
    elif n < 10:
        answer = 12000 * n + 2000 * k
    return answer
