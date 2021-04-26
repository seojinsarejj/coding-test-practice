#1차 --- 31.3 / 100.0
# count = 0

# def solution(n):
    
#     def dfs(x,sum,n):
    
#         sum = sum + x
#         if sum >= n :
#             if sum == n:
#                 global count
#                 count += 1
                
#             print(x)
#             return True

#         dfs(1,sum,n)
#         dfs(2,sum,n)
#         return True
    
#     global count
    
#     dfs(1,0,n)
#     dfs(2,0,n)
    
#     return count%1234567


# 다른 사람의 풀이
# n과 같이 변수의 조건의 범위가 크거나 1234567와 같이 결과값이 커서 나머지를 출력하라는 문제 거의 대부분은 DP 문제 입니다.
# 일반적인 완전 탐색의 접근법으로는 시간 초과가 나서 테스트 케이스를 전부 통과할 수 없습니다.
# 따라서, 멀리 뛰기 문제도 DP로 접근합니다.
# 규칙 : 피보나치 수열
def other_solution(n): 
    
    temp = [1,1]
    
    for i in range(2, n+1): 
        temp.append(temp[i-1] + temp[i-2]) 
        
    answer = temp[n] % 1234567     
    return answer


print(solution(20))
  