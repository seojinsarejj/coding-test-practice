# 1차 --- 40.0 / 100.0
# def solution(info, query):
     
#     result = []
#     applicant = [[j.strip() for j in i.split()] for i in info]

    
#     for q in query:

#         count = 0
#         condition = [i.strip() for i in q.split('and')]
#         condition = condition[:-1] + condition[-1].split()

#         condition = [i for i in condition[:-1] if i != '-'] + [condition[-1]]

#         for a in applicant :

#             if set(a) & set(condition[:-1]) == set(condition[:-1]) :
#                 if condition[-1] != "-" :
#                     if int(a[-1]) >= int(condition[-1]) :
#                         count += 1
#                 elif condition[-1] == "-" :
#                     count += 1

#         result.append(count)

#     return result 

# 2차 --- 40.0 / 100.0
def solution(info, query):
     
    result = []
    
    info = [i.split() for i in info]
    info_set = [set(i) for i in info]
    info_score = [int(i[-1]) for i in info]
    
    query = [q.split('and') for q in query]
    query = [q[:-1] + q[-1].split() for q in query]
    query = [[i.strip() for i in q if "-" not in i] for q in query]
    
    query_set = [set(q[:-1]) for q in query]
    query_score = [int(q[-1]) for q in query]
    
    
    for q,q_score in zip(query_set,query_score):

        count = 0

        for applicant,a_score in zip(info_set,info_score) :
            
            if applicant & q == q and a_score >= q_score :
                count += 1

        result.append(count)

    return result

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]

query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
            
            
print(solution(info,query))
        