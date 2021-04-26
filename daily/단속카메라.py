#1차 --- 0.0 / 100.0
def solution(routes):
    
    r = []
    
    for route in routes:
        r += route
    
    idx = min(r)
    
    cameras = [1 for _ in range(idx,max(r)+1)]
    
    for i in range(len(cameras)):
        
        cameras[i] = 0
        
        for route in routes:
            if cameras[route[0]-idx:route[1]+1-idx].count(1) == 0:
                cameras[i] = 1
    
    return cameras.count(1)
                
        
                
        