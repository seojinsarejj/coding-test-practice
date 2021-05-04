# 1차 --- 성공
def solution(n, s):
    
    if n > s:
        return [-1]

    base = s // n
    result = [base for _ in range(n)]

    remain = s % n

    for i in range(1,remain+1):
        result[i * (-1)] += 1

    return result


