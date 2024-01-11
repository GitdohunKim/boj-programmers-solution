def solution(num_list):
    m = 1
    s = 0
    for i in range(len(num_list)):
        m *= num_list[i]
        s += num_list[i]
    if m > s **2:
        return 0
    return 1