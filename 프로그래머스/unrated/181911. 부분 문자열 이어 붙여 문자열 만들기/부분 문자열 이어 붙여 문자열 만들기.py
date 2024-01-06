def solution(my_strings, parts):
    result = []
    for i in range(len(my_strings)):
        string = my_strings[i]
        part = parts[i]
        substring = string[part[0]:part[1]+1]
        result.append(substring)
    return ''.join(result)
