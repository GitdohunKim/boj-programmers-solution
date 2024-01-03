def solution(strArr):
    result = []
    for string in strArr:
        if "ad" not in string:
            result.append(string)
    return result
