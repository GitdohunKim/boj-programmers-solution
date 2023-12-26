row, column = map(int, input().split())

cheese_map = []
for x in range(row):
    cheese_map.append(list(map(int, input().split())))
c = []
for x in cheese_map:
    x [0] = 3
    x [-1] = 3
    c.append(x)
try:
    c[0] = [3 for _ in range(len(c[1]))]
    c[-1] = [3 for _ in range(len(c[1]))]
except :
    pass

def check(array):
    index = []
    for r in range(len(array)):
        for c in range(len(array[0])):
            if array[r][c] == 1:
                index.append([c, r])
    return check_2(index)

def check_2(dmp):
    out_list = []
    for x in dmp:
        m = False
        u = [x[1], x[0] - 1]
        l = [x[1] - 1, x[0]]
        r = [x[1] + 1, x[0]]
        d = [x[1], x[0] + 1]
        if c[u[0]][u[1]] == 3:
            m = True
        if c[r[0]][r[1]] == 3:
            m = True
        if c[d[0]][d[1]] == 3:
            m = True
        if c[l[0]][l[1]] == 3:
            m = True
        if m:
            out_list.append(x)
    return out_list

def condition3(arr):
    for r in range (1, len(arr)):
        for c in range (1, len(arr[0])):
            if arr[r][c] == 0:
                if arr[r+1][c] == 3 or arr[r][c+1] ==3 or arr[r-1][c] ==3 or arr[r][c-1] == 3:
                    return True

def search3(arr):
    if condition3(arr):
        for r in range (1, len(arr)):
            for c in range (1, len(arr[0])):
                if arr[r][c] == 0:
                    if arr[r+1][c] == 3 or arr[r][c+1] ==3 or arr[r-1][c] ==3 or arr[r][c-1] == 3:
                        arr[r][c] = 3
        for r in range (len(arr)-1, 0, -1):
            for c in range (len(arr[0]) -1, 0, -1):
                if arr[r][c] == 0:
                    if arr[r+1][c] == 3 or arr[r][c+1] ==3 or arr[r-1][c] ==3 or arr[r][c-1] == 3:
                        arr[r][c] = 3
        return search3(arr)

def change(arr):
    for r in range(len(arr)):
        for c in range(len(arr[0])):
            if arr[r][c] == 2:
                arr[r][c] = 3

def main(arr):
    global time
    num1 = 0
    num2 = 0
    for r in range(len(arr)):
        for c in range(len(arr[0])):
            if arr[r][c] == 1:
                num1 += 1
            elif arr[r][c] == 2:
                num2 += 1
    if num1 == 0:
        return [time, num2]
    else :
        change(arr)
        search3(arr)
        search3(arr)
        for x in check(arr):
            arr[x[1]][x[0]] = 2
        time += 1
        return main(arr)

time = 0
for x in main(c):
    print(x)