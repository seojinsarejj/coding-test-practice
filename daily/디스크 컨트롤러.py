# 1차 --- 15.0 / 100.0
# import heapq
# def solution(jobs):
    
#     count = len(jobs)

#     progress = []
#     waiting = []
#     result = []
#     time = -1
    
    
#     while waiting or jobs or progress:
        
#         time += 1
        
#         if progress:

#             if progress[0][2] + progress[0][0] == time:
#                 end = progress.pop()
#                 result.append(time - end[1])

#         if jobs: 
        
#             if jobs[0][0] == time:

#                 start,during = heapq.heappop(jobs)
#                 heapq.heappush(waiting,[during,start])

#         if len(progress) == 0 and waiting:
#             during,start = heapq.heappop(waiting)
#             progress.append((during,start,time))
                
#     return sum(result) // count
        
# 다른 사람의 풀이
def solution(jobs):
    answer = 0
    start = 0  # 현재까지 진행된 작업 시간
    length = len(jobs)

    jobs = sorted(jobs, key=lambda x: x[1])  # 소요시간 우선 정렬

    while len(jobs) != 0:
        for i in range(len(jobs)):
            if jobs[i][0] <= start:
                start += jobs[i][1]
                answer += start - jobs[i][0]
                jobs.pop(i)
                break
            # 해당시점에 아직 작업이 들어오지 않았으면 시간 ++
            if i == len(jobs) - 1:
                start += 1

    return answer // length


print(solution([[0, 3], [1, 9], [2, 6]]	))