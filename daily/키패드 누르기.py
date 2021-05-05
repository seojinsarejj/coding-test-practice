# 1차 --- 성공
def solution(numbers, hand):
    
    result = ""
    l_loc = [3,0]
    r_loc = [3,2]
    
    for num in numbers:
        
        if num in [1,4,7] :
            result += "L"
            l_loc = [num // 3 , 0]
        elif num in [3,6,9] :
            result += "R"
            r_loc = [num // 3 - 1 , 2]
        else :
            target = [num // 3 , 1]
            if num == 0:
                target = [3, 1]
                
            l_dis = abs(l_loc[0] - target[0]) + abs(l_loc[1] - target[1])
            r_dis = abs(r_loc[0] - target[0]) + abs(r_loc[1] - target[1])
            
            if l_dis < r_dis or l_dis == r_dis and hand == "left":
                result += "L"
                l_loc = target
            elif r_dis < l_dis or l_dis == r_dis and hand == "right":
                result += "R"
                r_loc = target
            
            
    return result
                    