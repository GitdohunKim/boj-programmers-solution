import sys

N = int(input())

numbers = []
for i in range(0,N):
    number = int(sys.stdin.readline().strip())
    numbers.append(number)

numbers.sort()
for num in numbers:
    print(num)