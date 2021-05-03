# 1차 --- 성공
def solution(N, stages):
    
    result = []
    
    for i in range(1,N+1):
        
        challenger = [n for n in stages if n >= i]
        not_clear = [n for n in challenger if n == i]
        
        if len(challenger) == 0 :
            score = 0
        else :
            score = len(not_clear)/len(challenger)
        result.append((i,score))
        
    result.sort(key=lambda x : x[1],reverse=True)
    return [i[0] for i in result]
