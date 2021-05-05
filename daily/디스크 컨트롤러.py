# 1차 --- 15.0 / 100.0
import heapq
def solution(jobs):
    
    count = len(jobs)

    progress = []
    waiting = []
    result = []
    time = -1
    
    
    while waiting or jobs or progress:
        
        time += 1
        
        if progress:

            if progress[0][2] + progress[0][0] == time:
                end = progress.pop()
                result.append(time - end[1])

        if jobs: 
        
            if jobs[0][0] == time:

                start,during = heapq.heappop(jobs)
                heapq.heappush(waiting,[during,start])

        if len(progress) == 0 and waiting:
            during,start = heapq.heappop(waiting)
            progress.append((during,start,time))
                
    return sum(result) // count
        

print(solution([[0, 3], [1, 9], [2, 6]]	))