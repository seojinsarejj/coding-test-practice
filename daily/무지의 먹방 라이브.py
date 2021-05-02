# 1차 --- 24.1 / 100.0
# def solution(food_times,k):
    
#     length = len(food_times)
    
#     index = 0
#     count = 0
    
#     while True:
        
#         index += 1
        
#         if count >= k or sum(food_times) == 0:
#             break
    
#         seq = index % length
        
#         if seq == 0:
#             idx = -1
#         else: 
#             idx = seq - 1
        
#         if food_times[idx] == 0:
#             continue
            
#         food_times[idx] -= 1
#         count += 1
        
    
#     if sum(food_times) == 0:
#         return -1
    
#     seq = index % length

#     if seq == 0:
#         idx = -1
#     else: 
#         idx = seq - 1
    
#     return idx + 1


# 2차 --- 28.1 / 100.0
# def solution(food_times,k):

#     index = -1
#     count = 0
#     length = len(food_times)

#     while True:

#         index += 1

#         if count >= k or sum(food_times) == 0:
#             break

#         if food_times[index%length] == 0:
#             continue

#         food_times[index%length] -= 1
#         count += 1


#     if sum(food_times) == 0:
#         return -1

#     return index%length + 1

# 정답
import heapq

def solution(food_times, k):
    
    if sum(food_times) <= k:
        return -1
    
    queue = []
    
    for i,time in enumerate(food_times):
        heapq.heappush(queue, (time,i))
        
    while True:
        if queue[0][0] * len(queue) > k:
            print(queue)
            break
        food = heapq.heappop(queue)
        k -= food[0] * (len(queue) + 1)
        
    result = sorted(queue, key=lambda x : x[1])
    print(result)
    return result[k % len(queue)][0]
    
print(solution([3, 1, 2],5))
    
