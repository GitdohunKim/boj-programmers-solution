import sys

while True:
    num = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    sortlist = sorted(num)

    if sortlist == [0, 0, 0]:
        break
    if sortlist[2] ** 2 == (sortlist[0] ** 2) + (sortlist[1] ** 2):
        print("right")
    else:
        print("wrong")