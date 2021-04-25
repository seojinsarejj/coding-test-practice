#1차
def solution(dartResult):
    
    score = []
    result = []
    
    for c in dartResult:
        
        if c in "0123456789":
            
            score.append(c)
            
        elif c in "SDT" :
            
            s = int("".join(score))
            s = s if c == "S" else s**2 if c == "D" else s**3
            result.append(s)
            score = []
            
        elif c in "*#":
            
            if c == "*" :
                result = result[:-2] + [r*2 for r in result[-2:]]
            else:
                result[-1] = result[-1] * (-1)
                
                
    return sum(result)
    
    