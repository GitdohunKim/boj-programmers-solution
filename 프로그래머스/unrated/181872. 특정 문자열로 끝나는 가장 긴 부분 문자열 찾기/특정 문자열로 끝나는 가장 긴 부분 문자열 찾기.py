def solution(myString, pat):
    longest_substring = ''
    for i in range(len(myString), 0, -1): 
        substring = myString[:i]
        if substring.endswith(pat):
            longest_substring = substring
            break
    return longest_substring
