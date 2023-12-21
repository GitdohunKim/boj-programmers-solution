def solution(N, number):
    num_set = [set() for _ in range(9)]
    for i in range(1, 9):
        num_set[i].add(int(str(N) * i))
    
    for i in range(2, 9):
        for j in range(1, i):
            for num1 in num_set[j]:
                for num2 in num_set[i - j]:
                    num_set[i].add(num1 + num2)
                    num_set[i].add(num1 - num2)
                    num_set[i].add(num1 * num2)
                    if num2 != 0:
                        num_set[i].add(num1 // num2)
    
    for i in range(1, 9):
        if number in num_set[i]:
            return i
    
    return -1
