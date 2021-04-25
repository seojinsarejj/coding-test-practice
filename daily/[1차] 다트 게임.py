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
    
# 다른 사람의 풀이
import re


def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer