# 1차 --- 성공
from collections import deque
def solution(n, vertex):
    
    graph = [[] for _ in range(n)]
    
    visited = [-1 for _ in range(n)]
    visited[0] = 0
    
    for v in vertex:
        graph[v[0]-1].append(v[1])
        graph[v[1]-1].append(v[0])
        
    queue = deque([1])
    count = 0
    
    print(visited)
    
    while queue:
        
        count += 1
        
        for _ in range(len(queue)):
            start = queue.popleft()

            for g in graph[start-1]:
                if visited[g-1] == -1:
                    queue.append(g)
                    visited[g-1] = count
        
        
    far = max(visited)
    
    return len([i for i in visited if i == far])
            
    
        
        
    