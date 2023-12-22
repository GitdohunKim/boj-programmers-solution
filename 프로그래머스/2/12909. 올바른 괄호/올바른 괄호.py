def solution(s):
    rest = 0
    for i in s:
        if i == "(":
            rest += 1          

        elif i == ")":
            rest -= 1
            
        if rest < 0:
            return False

    if rest != 0:
        return False

    return True