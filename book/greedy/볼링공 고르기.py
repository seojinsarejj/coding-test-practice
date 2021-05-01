# 나의 풀이
def solution(balls):

    count = 0

    for i in range(len(balls)-1):
        for ball in balls[i+1:]:
            if balls[i] != ball:
                count += 1

    return count


print(solution([1,5,4,3,2,4,5,2]))

# 정답
def answer(balls):

    n = len(balls)
    m = max(balls)
    array = [0] * 11

    for x in balls:
        array[x] += 1

    result = 0

    for i in range(1, m + 1):
        n -= array[i]
        result += array[i] * n

    print(result)

        
