def solution(left, right):
    def count_factors(num):
        count = 0
        for i in range(1, int(num ** 0.5) + 1):
            if num % i == 0:
                count += 1
                if i != num // i:
                    count += 1
        return count
    
    answer = 0
    for num in range(left, right + 1):
        if count_factors(num) % 2 == 0:
            answer += num
        else:
            answer -= num

    return answer
