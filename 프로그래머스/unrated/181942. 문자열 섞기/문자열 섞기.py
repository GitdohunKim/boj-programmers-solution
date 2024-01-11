def solution(str1, str2):
    answer = ""
    for char1, char2 in zip(str1,str2):
        answer += char1+char2
    return answer