def CCW(p1_x, p1_y, p2_x, p2_y, p3_x, p3_y):
    ccw = (p2_x-p1_x)*(p3_y-p1_y)-(p3_x-p1_x)*(p2_y-p1_y)
    if ccw:
        ccw //= abs(ccw)
    return ccw

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
ccw3 = CCW(x1, y1, x2, y2, x3, y3)
ccw4 = CCW(x1, y1, x2, y2, x4, y4)
ccw1 = CCW(x3, y3, x4, y4, x1, y1)
ccw2 = CCW(x3, y3, x4, y4, x2, y2)
if ccw1 * ccw2 == 1 or ccw3 * ccw4 == 1:
    print(0)
elif ccw1 == 0 and ccw2 == 0:
    if x1 == x2:
        if max(y1, y2) < min(y3, y4) or max(y3, y4) < min(y1, y2):
            print(0)
        elif max(y1, y2) == min(y3, y4):
            print(1)
            print(x1, max(y1, y2))
        elif max(y3, y4) == min(y1, y2):
            print(1)
            print(x1, min(y1, y2))
        else:
            print(1)
    else:
        if max(x1, x2) < min(x3, x4) or max(x3, x4) < min(x1, x2):
            print(0)
        elif max(x1, x2) == min(x3, x4):
            print(1)
            if x1 > x2:
                print(x1, y1)
            else:
                print(x2, y2)
        elif max(x3, x4) == min(x1, x2):
            print(1)
            if x1 < x2:
                print(x1, y1)
            else:
                print(x2, y2)
        else:
            print(1)
else:
    print(1)
    if x1 == x2:
        a2 = (y4 - y3) / (x4 - x3)
        b2 = y3 - a2 * x3
        print(x1, a2 * x1 + b2)
    elif x3 == x4:
        a1 = (y2 - y1) / (x2 - x1)
        b1 = y1 - a1 * x1
        print(x3, a1 * x3 + b1)
    else:
        a1 = (y2 - y1) / (x2 - x1)
        b1 = y1 - a1 * x1
        a2 = (y4 - y3) / (x4 - x3)
        b2 = y3 - a2 * x3
        print((b2 - b1) / (a1 - a2), a1 * (b2 - b1) / (a1 - a2) + b1)