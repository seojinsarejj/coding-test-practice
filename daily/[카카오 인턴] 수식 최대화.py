# 1차 --- 36.7 / 100.0
# from itertools import permutations
# import re
# def solution(expression):
    
#     result = 0
#     ops_all = re.findall("[+*-]", expression)
#     ops = set(ops_all)

#     for op in permutations(ops, len(ops)):

#         exp = expression
#         for o in op:

#             for _ in range(ops_all.count(o)) :

#                 target = re.findall("-?\d+[" + o + "]-?\d+",exp)

#                 t = eval(target[0])
#                 exp = exp.replace(target[0],str(t))
#         if abs(int(exp)) >= result :
#             result = abs(int(exp))


#     return result

# 2차 --- 50.0 / 100.0
from itertools import permutations
import re
def solution(expression):
    
    result = 0
    ops_all = re.findall("[+*-]", expression)
    ops = set(ops_all)

    for op in permutations(ops, len(ops)):
        exp = expression
        for o in op:
            for _ in range(ops_all.count(o)) :
                target = re.findall("\d+[" + o + "]-?\d+",exp)
                if target[0] == exp[1:len(target[0])+1]:
                    target[0] = "-" + target[0] 
                t = str(eval(target[0]))
                exp = exp.replace(target[0],t)
        if abs(int(exp)) >= result :
            result = abs(int(exp))

    return result




# 다른 사람의 풀이
from itertools import permutations
import re

def other_solution(expression):
    expressions = set(re.findall("\D", expression))
    prior = permutations(expressions)
    cand = []

    for op_cand in prior:
        temp = re.compile("(\D)").split('' + expression)
        for exp in op_cand:
            while exp in temp:
                idx = temp.index(exp)
                temp = temp[:idx-1] + [str(eval(''.join(temp[idx-1:idx+2])))] + temp[idx+2:]
        cand.append(abs(int(temp[0])))
    return max(cand)

print(other_solution("100-200*300-500+20"))