# 1차 --- 성공
def solution(s):
    
    for count in range(len(s),1,-1):
        
        for i in range(len(s)-count+1):
            
            target = s[i:i+count]
            palindrome = True
            for j in range(count//2):
                
                if target[j] != target[(j+1) * (-1)]:
                    palindrome = False
                    break
            
            if palindrome == True:
                return count
        
    return 1
        

# 다른 사람의 풀이
def longest_palindrom(s):
    
    return len(s) if s[::-1] == s else max(longest_palindrom(s[:-1]), longest_palindrom(s[1:]))
