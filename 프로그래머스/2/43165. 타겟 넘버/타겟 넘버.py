def solution(numbers, target):
    count = 0
    n = len(numbers)

    for i in range(2 ** n):
        current_sum = 0
        for j in range(n):
            if (i >> j) & 1:
                current_sum += numbers[j]
            else:
                current_sum -= numbers[j]
        
        if current_sum == target:
            count += 1

    return count
