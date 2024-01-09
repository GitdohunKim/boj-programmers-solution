def solution(my_string, index_list):
    answer = []
    list_1 = list(my_string)
    for i in index_list:
        answer.append(list_1[i])
    return ''.join(answer)
