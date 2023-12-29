import sys


def solution():
    n, *nums = map(int, sys.stdin.buffer.read().splitlines())
    stack, result = [], []
    num = 1
    for value in nums:
        while num <= value:
            stack.append(num)
            result.append('+')
            num += 1
        if stack.pop() != value:
            return 'NO'
        result.append('-')
    return '\n'.join(result)

print(solution())