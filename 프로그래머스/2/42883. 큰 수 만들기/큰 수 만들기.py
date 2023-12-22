def solution(number, k):
    stack = []

    for num in number:
        while stack and k > 0 and stack[-1] < num:
            stack.pop()
            k -= 1

        stack.append(num)
        
    stack = stack[:-k] if k > 0 else stack

    return ''.join(stack)
