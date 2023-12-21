def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    food_list = [(time, i+1) for i, time in enumerate(food_times)]
    food_list.sort()
    length = len(food_list)
    previous = 0
    
    for i, (time, index) in enumerate(food_list):
        diff = time - previous
        curr_time = diff * length
        if curr_time <= k:
            k -= curr_time
            previous = time
        else:
            remaining = [(index, time) for time, index in food_list[i:]]
            remaining.sort(key=lambda x: x[0])
            return remaining[k % len(remaining)][0]
        
        length -= 1
    
    return -1