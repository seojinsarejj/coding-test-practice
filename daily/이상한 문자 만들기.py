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


def other_solution(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))



print(solution("Seo Jinaefv"))


