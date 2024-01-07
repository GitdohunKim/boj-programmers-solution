import sys

def solution(x1, y1, x2, y2, x3, y3, x4, y4):
    ccw123 = ccw(x1, y1, x2, y2, x3, y3)
    ccw124 = ccw(x1, y1, x2, y2, x4, y4)
    ccw341 = ccw(x3, y3, x4, y4, x1, y1)
    ccw342 = ccw(x3, y3, x4, y4, x2, y2)

    if ccw123 * ccw124 == 0 and ccw341 * ccw342 == 0:
        if min(x1, x2) <= max(x4, x3) and min(y1, y2) <= max(y4, y3) and min(x3, x4) <= max(x2, x1) and min(y3, y4) <= max(y2, y1):
            return 1
    else:
        if ccw123 * ccw124 <= 0 and ccw341 * ccw342 <= 0:
            return 1

    return 0


def ccw(x1, y1, x2, y2, x3, y3):
    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)


if __name__ == '__main__':
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())

    print(solution(x1, y1, x2, y2, x3, y3, x4, y4))
