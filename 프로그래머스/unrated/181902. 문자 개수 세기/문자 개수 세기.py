def solution(my_string):
    count = [0] * 52  # 알파벳 개수를 담을 배열 초기화
    
    for char in my_string:
        if char.isupper():  # 대문자인 경우
            index = ord(char) - ord('A')  # 알파벳 인덱스 계산
            count[index] += 1
        elif char.islower():  # 소문자인 경우
            index = ord(char) - ord('a') + 26  # 알파벳 인덱스 계산
            count[index] += 1
    
    return count