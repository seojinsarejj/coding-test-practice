#1차 --- 성공
def solution(s):
    
    words = s.split(" ")
    
    result = []
    
    for word in words:
        target = ""
        for i in range(len(word)):
            c = word[i]
            if i % 2 == 0 :
                c = c.upper()
            else :
                c = c.lower()
            target += c
            
        result.append(target)
        
    return " ".join(result)


print(solution("Seo Jinaefv"))