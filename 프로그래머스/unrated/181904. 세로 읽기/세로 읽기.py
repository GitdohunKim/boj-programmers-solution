def solution(my_string, m, c):
    result = ""
    for i in range(c-1, len(my_string), m):
        result += my_string[i]
    return result
