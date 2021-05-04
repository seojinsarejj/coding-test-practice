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


# 다른 사람의 풀이
def bestSet(n, s):
    answer = []
    a = int(s/n)

    if a == 0:
        return [-1]

    b = s%n

    for i in range(n-b):
        answer.append(a)
    for i in range(b):
        answer.append(a+1)

    return answer