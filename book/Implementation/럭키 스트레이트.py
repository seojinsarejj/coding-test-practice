def solution(n):

    mid = len(n) // 2

    left = sum([int(n) for n in n[:mid]])
    right = sum([int(n) for n in n[mid:]])

    if left == right :
        print("LUCKY")
    else:
        print("READY")


solution("123402")
solution("7755")

    
