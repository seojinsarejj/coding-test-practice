def solution(n,coins):

    coins.sort()

    target = 1
    for c in coins:
        if c > target:
            return target
        target += c

    return 0


print(solution(5,[3,2,1,1,9]))

