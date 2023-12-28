n = int(input())
for i in range(n):
    grade_list = list(input())
    total = sum = 0
    for ox in grade_list:
        if (ox == 'O'):
            sum += 1
            total += sum
        else:
            sum = 0
    print(total)