def solution(s):

    alpha = [c for c in s if c.isalpha()]
    num = [c for c in s if c in "0123456789"]

    return "".join(sorted(alpha)) + str(sum([int(n) for n in num]))

print(solution("K1KA5CB7"))