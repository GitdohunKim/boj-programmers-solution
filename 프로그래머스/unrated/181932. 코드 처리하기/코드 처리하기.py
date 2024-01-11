def solution(code):
    mode = 0
    answer = [] 
    for i in range(len(code)):
        if code[i]=="1":
            mode = (mode+1)%2
            continue
        if mode == 0 and i % 2 == 0:
            answer.append(code[i])
        elif mode == 1 and i % 2 == 1:
            answer.append(code[i])
        else:
            continue
    if not answer:
        return "EMPTY"
    return ''.join(answer)
