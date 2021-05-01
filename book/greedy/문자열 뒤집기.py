def solution(s):

    zero = s.split("1")
    zero = [i for i in zero if i != '']
    zero = len(zero)

    one = s.split("0")
    one = [i for i in one if i != '']
    one = len(one)

    return min(zero,one)

print(solution("0001100"))