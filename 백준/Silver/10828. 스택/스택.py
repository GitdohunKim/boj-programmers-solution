import sys
arr = []


def push(num):
    arr.append(num)

def pop():
    if not arr:
        print(-1)
    else:
        print(arr.pop())


def size():
    print(len(arr))


def empty():
    if not arr:
        print(1)
    else:
        print(0)


def top():
    if not arr:
        print(-1)
    else:
        print(arr[-1])


N = int(sys.stdin.readline().rstrip())
for i in range(N):
    function = sys.stdin.readline().rstrip()
    if function == 'top':
        top()
    elif function == 'empty':
        empty()
    elif function == 'size':
        size()
    elif function == 'pop':
        pop()
    else:
        function = function.split()
        num = int(function[1])
        push(num)
