# 1차 --- 성공
def solution(new_id):
    
    new_id = str(new_id.lower())
    print(new_id)
    
    new_id = ''.join([c for c in new_id if c.isalpha() or c.isdigit() or c in "-_."])
    
    new_id = ".".join([c for c in new_id.split(".") if c != ''])
    
    if new_id == "":
        new_id = "a" 

    new_id = new_id[:15]

    if new_id[-1] == ".":
        new_id = new_id[:-1] 

    while len(new_id) <= 2:
        new_id += new_id[-1]

    return new_id
    