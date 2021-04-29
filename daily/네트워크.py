#1차 --- 성공
def solution(n, computers):
    
    
    def network(start,computers,visited):
        
        visited[start] = 1
        
        for i in range(len(computers[start])):
            if computers[start][i] == 1 and visited[i] == 0:
                network(i,computers,visited)
                
        return True
        
            
    count = 0
    visited = [0 for _ in range(n)]
    
    for i in range(n):
        if visited[i] == 1:
            continue
            
        network(i,computers,visited)
        count += 1
        
    return count
        
print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))