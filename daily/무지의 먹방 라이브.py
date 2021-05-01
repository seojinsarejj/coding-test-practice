# 1차 --- 5.4 / 100.0
def solution(food_times,k):
    
    length = len(food_times)
    
    index = 0
    count = 0
    
    while True:
        
        index += 1
        
        if count >= k or sum(food_times) == 0:
            break
    
        seq = index % length
        
        if seq == 0:
            idx = -1
        else: 
            idx = seq - 1
        
        if food_times[idx] == 0:
            continue
            
        food_times[idx] -= 1
        count += 1
        
    
    if sum(food_times) == 0:
        return -1
    
    seq = index % length

    if seq == 0:
        idx = -1
    else: 
        idx = seq - 1
    
    return food_times[idx]
