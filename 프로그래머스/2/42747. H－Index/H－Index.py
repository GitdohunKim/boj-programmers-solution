def solution(citations):
    citations.sort()  
    n = len(citations) 

    h_index = 0  

    for i in range(n):
        if citations[i] >= n - i:  
            h_index = max(h_index, n - i)  

    return h_index
