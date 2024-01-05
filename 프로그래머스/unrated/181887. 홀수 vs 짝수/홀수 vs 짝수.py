def solution(num_list):
    odd = sum(num_list[::2])
    even = sum(num_list[1::2])
    if odd >= even:
        return odd
    else:
        return even