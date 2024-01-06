def solution(my_string):
    suffixes = []
    for i in range(len(my_string)):
        suffixes.append(my_string[i:])
    return sorted(suffixes)
