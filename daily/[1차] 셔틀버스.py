# 1차 --- 성공
import heapq
def solution(n, t, m, timetable):
    
    
    arrive_time = [540 + i * t for i in range(n)]
    _timetable = []
    waiting = []
    
    for time in timetable:
        
        hour,minit = time.split(":")
        heapq.heappush(_timetable,int(hour) * 60 + int(minit))
    
    
    board = 0
    
    for at in arrive_time :
        
        while _timetable:
            
            if _timetable[0] > at:
                break
            t = heapq.heappop(_timetable)
            heapq.heappush(waiting,t)
        
        if at == arrive_time[-1] :
            if len(waiting) >= m:
                for _ in range(m):
                    last = heapq.heappop(waiting)
                board =  last - 1
            else :
                board =  at
                
        
        if len(waiting) > m:
            for _ in range(m):
                heapq.heappop(waiting)
        else:
            waiting = []
    
    hour,minit = divmod(board,60)
    
    return str(hour).zfill(2) + ":" + str(minit).zfill(2)