# 다른 사람의 풀이 
from itertools import permutations
def solution(user_id, banned_id):
    
    def isMatched(user,_id):
        
        for i in range(len(_id)):
            if _id[i] != "*" and user[i] != _id[i] :
                return False
        
        return True
        
    
    def check(users,banned_id):
        
        for i in range(len(banned_id)):
            
            if len(users[i]) != len(banned_id[i]):
                return False
            if not isMatched(users[i],banned_id[i]):
                return False
            
        return True
            
    result = []
    
    for users in permutations(user_id,len(banned_id)):
        if check(users,banned_id):
            users = set(users)
            if users not in result:
                result.append(users)
            
    return len(result)
        
    
    