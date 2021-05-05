# 1차
def solution(n, arr1, arr2):

    
    _arr1 = []
    _arr2 = []
    
    for i in range(n):
        _arr1.append(bin(arr1[i])[2:].zfill(n))
        _arr2.append(bin(arr2[i])[2:].zfill(n))

    result = []
    
    for i in range(n):
        row = ""
        for j in range(n):
            if _arr1[i][j] == "1" or _arr2[i][j] == "1":
                row += "#"
            else:
                row += " "
        result.append(row)
        
    return result

print(solution(6,[46, 33, 33 ,22, 31, 50],[27 ,56, 19, 14, 14, 10]))