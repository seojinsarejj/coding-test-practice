#1차 --- 31.3 / 100.0
count = 0

def solution(n):
    
    def dfs(x,sum,n):
    
        sum = sum + x
        if sum >= n :
            if sum == n:
                global count
                count += 1
            return True

        dfs(1,sum,n)
        dfs(2,sum,n)
    
    global count
    
    dfs(1,0,n)
    dfs(2,0,n)
    
    return count%1234567
  