import sys

def find_largest_area(lst):
    stack = []
    max_area = 0
    n = len(lst)

    for i in range(n):
        idx = i
        while stack and stack[-1][1] > lst[i]:
            idx, height = stack.pop()
            area = (i - idx) * height
            max_area = max(max_area, area)
        stack.append([idx, lst[i]])

    while stack:
        idx, height = stack.pop()
        area = (n - idx) * height
        max_area = max(max_area, area)

    return max_area

def main():
    N = int(sys.stdin.readline())
    lst = []
    for _ in range(N):
        num = int(sys.stdin.readline())
        lst.append(num)

    result = find_largest_area(lst)
    print(result)

main()
