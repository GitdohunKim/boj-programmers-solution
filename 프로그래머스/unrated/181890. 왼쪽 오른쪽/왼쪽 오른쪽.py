def solution(str_list):
    answer = []
    i = 0
    while i < len(str_list):
        if str_list[i] == 'l':
            answer = str_list[:i]
            break
        elif str_list[i] == 'r':
            answer = str_list[i + 1:]
            break
        i += 1
    return answer
