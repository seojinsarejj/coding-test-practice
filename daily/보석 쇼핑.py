# 1차 --- 28.9 / 100.0
def solution(gems):
    
    gem_kind = set(gems)
    
    for length in range(len(gem_kind),len(gems)):
        
        for i in range(len(gems) - length + 1):
            
            if len(set(gems[i:i+length])) == len(gem_kind):
                return [i+1,i+length]
            
    return [1,len(gems)]