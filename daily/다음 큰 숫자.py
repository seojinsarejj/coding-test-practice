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
        