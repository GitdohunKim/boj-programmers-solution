def solution(myStr):
    result = [myStr] 
    separators = ["a", "b", "c"]
    
    for sep in separators:
        temp = []
        for substr in result:
            temp.extend(substr.split(sep))
        result = temp
    
    result = [x for x in result if x]  
    
    if not result: 
        return ["EMPTY"]
    
    return result

