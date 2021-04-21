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


print(solution("100-200*300-500+20"))