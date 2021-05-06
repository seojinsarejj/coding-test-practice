# 1차 --- 86.4 / 100.0
def solution(lines):
    
    timeline = []
    result = []
    
    for line in lines:
        date, time, during = line.split(" ")
        
        hour,mint,sec = time.split(":")
        
        end = (int(hour) * 3600 + int(mint) * 60 + float(sec)) * 1000
        start = end - float(during[:-1]) * 1000 + 1
        timeline.append([start,end])
        
    r = 1
    for time in timeline:
        
        start = time[0]
        end = start + 1000
        count = 1
        
        for t in timeline:
            if t[1] >= start and t[0] < end:
                count += 1
        
        s = count
        
        start = time[1]
        end = start + 1000
        count = 0
        
        for t in timeline:
            if t[1] >= start and t[0] < end:
                count += 1
        
        e = count
        
        r = max(r,s,e)
        
    return r - 1
        