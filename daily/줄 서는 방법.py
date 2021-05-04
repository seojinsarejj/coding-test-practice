# 1차 --- 63.2 / 100.0ㄴ
# from itertools import permutations
# def solution(n, k):
    
#     people = [i for i in range(1,n + 1)]
    
#     per = list(permutations(people))
    
#     return list(per[k-1])
    
# 2차 --- 성공
from math import factorial
def solution(n, k):
    
    people = [i for i in range(1,n + 1)]
    count = factorial(n)
    
    answer = []
    
    for _ in range(n-1):
        
        p = people[(k-1) // (count // n)]
        answer.append(p)
        k = k % (count // n)
        count = count // n
        n -= 1
        people.remove(p)
    
    answer.append(people[0])
    
    
    return answer