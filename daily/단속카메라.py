#1차 --- 0.0 / 100.0
# def solution(routes):
    
#     r = []
    
#     for route in routes:
#         r += route
    
#     idx = min(r)
    
#     cameras = [1 for _ in range(idx,max(r)+1)]
    
#     for i in range(len(cameras)):
        
#         cameras[i] = 0
        
#         for route in routes:
#             if cameras[route[0]-idx:route[1]+1-idx].count(1) == 0:
#                 cameras[i] = 1
    
#     return cameras.count(1)
                
        
                
#2차 --- 10.0 / 100.0
def solution(routes):
    
    rngs = []
    
    
    for route in routes :
        
        r = range(route[0],route[1]+1)
        
        isIn = False
        idx = 0
        
        for i in range(len(rngs)):
            
            if len(set(r) & set(range(rngs[i][0],rngs[i][1]+1))) == 0:
                isIn = False
            else:
                isIn = True
                idx = i
                break
                
        if isIn:
            rng = range(rngs[idx][0],rngs[idx][1]+1)
            new_rng = list(set(r) & set(rng))
            rngs[idx] = [min(new_rng),max(new_rng)]
        else:
            rngs.append(route)
            
    return len(rngs)
            
                
# 3차 --- 50.0 / 100.0
def solution(routes):
    
    routes.sort(key=lambda x : x[1])
    
    rngs = []
    
    
    for route in routes :
        
        r = range(route[0],route[1]+1)
        
        isIn = False
        idx = 0
        
        for i in range(len(rngs)):
            
            if len(set(r) & set(range(rngs[i][0],rngs[i][1]+1))) == 0:
                isIn = False
            else:
                isIn = True
                idx = i
                break
                
        if isIn:
            rng = range(rngs[idx][0],rngs[idx][1]+1)
            new_rng = list(set(r) & set(rng))
            rngs[idx] = [min(new_rng),max(new_rng)]
        else:
            rngs.append(route)
            
    return len(rngs)
            
                
print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))