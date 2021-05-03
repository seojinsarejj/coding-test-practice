# 1차 --- 96.0 / 100.0
# def solution(s):

   
#     answer = []

#     for i in range(1,len(s)//2+1):

#         stack = []
#         result = ""
#         idx = 0

#         while idx <= len(s):
            
#             c = s[idx:idx+i]
#             idx += i

#             if stack != [] :
#                 if stack[0] != c:
#                     if len(stack) == 1:
#                         result += stack[0]
#                     else:
#                         result += str(len(stack)) + stack[0]
#                     stack = []
            
#             stack.append(c)
        
        
#         result += "".join(stack)
            
#         answer.append(result)

#     return min([len(a) for a in answer])

# 2차 --- 성공
def solution(s):
    
    if len(s) == 1:
        return 1
    
    answer = []

    for i in range(1,len(s)//2+1):

        stack = []
        result = ""
        idx = 0

        while idx <= len(s):
            
            c = s[idx:idx+i]
            idx += i

            if stack != [] :
                if stack[0] != c:
                    if len(stack) == 1:
                        result += stack[0]
                    else:
                        result += str(len(stack)) + stack[0]
                    stack = []
            
            stack.append(c)
        
        
        result += "".join(stack)
            
        answer.append(result)

    return min([len(a) for a in answer])

print(solution("abcabcabcabcdededededede"))