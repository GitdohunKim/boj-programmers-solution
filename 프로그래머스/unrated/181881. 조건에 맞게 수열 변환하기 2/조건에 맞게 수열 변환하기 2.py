def solution(arr):
    i = 0
    while True:
        new_arr = []
        for num in arr:
            if num >= 50 and num % 2 == 0:
                new_arr.append(num // 2)
            elif num < 50 and num % 2 == 1:
                new_arr.append(num * 2 + 1)
            else:
                new_arr.append(num)
        if new_arr == arr:
            break
        arr = new_arr
        i += 1
    return i
