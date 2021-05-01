def solution(n,people):

    people.sort(reverse=True)

    count = 0

    stack = []

    for p in people:

        stack.append(p)

        if stack[0] <= len(stack):
            stack = []
            count += 1
        
    return count

print(solution(5,[2,3,1,2,2]))