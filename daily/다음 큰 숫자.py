# 1차 === 성공
def solution(n):
    
    n_b = format(n,'b')
    n_b = n_b.replace("0","")
    m = n
    
    while(True) :
        m = m + 1
        m_b = format(m,'b')
        m_b = m_b.replace("0","")
        if len(n_b) == len(m_b):
            break
            
    return m


# 다른 사람의 풀이
def nextBigNumber(n):
    c = bin(n).count('1')
    for m in range(n+1,2*n+1):
        if bin(m).count('1') == c:
            return m

        