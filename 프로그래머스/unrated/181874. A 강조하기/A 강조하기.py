def solution(myString):
    result = ""
    for char in myString.lower():
        if char == "a":
            result += char.upper()
        else:
            result += char
    return result