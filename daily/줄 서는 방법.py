# 1차 --- 63.2 / 100.0ㄴ
from itertools import permutations
def solution(n, k):
    
    people = [i for i in range(1,n + 1)]
    
    per = list(permutations(people))
    
    return list(per[k-1])
    
