def solution(operations):
    num_list = []
    for i in operations:
        if(i[0] == "I"):
            num = int(i[2:])
            num_list.append(num)
        else:
            if(i[2] == "-"):
                if(len(num_list) <= 1): 
                    num_list.clear()
                else:
                    min_num = min(num_list)
                    num_list.remove(min_num)
            else:
                if(len(num_list) <= 1): 
                    num_list.clear()
                else:
                    max_num = max(num_list)
                    num_list.remove(max_num)
    if (len(num_list) == 0):
        return [0,0]
    return [max(num_list), min(num_list)]