def solution(s):

    result = 0

    for num in s:

        n = int(num)

        if result <= 1 or n <= 1:
            result += n
        else:
            result *= n

    return result


print(solution("02984"))
