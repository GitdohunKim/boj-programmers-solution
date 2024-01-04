import sys

input = sys.stdin.readline

words = list(input().rstrip())
boom = input().rstrip()

stack = []
boom_len = len(boom)

for char in words:
    stack.append(char)
    if ''.join(stack[-boom_len:]) == boom:
        stack[-boom_len:] = []

result = ''.join(stack) if stack else "FRULA"
print(result)
