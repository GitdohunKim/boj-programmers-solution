def solution(intStrs, k, s, l):
    result = []
    for string in intStrs:
        substring = string[s:s+l]
        num = int(substring)
        if num > k:
            result.append(num)
    return result