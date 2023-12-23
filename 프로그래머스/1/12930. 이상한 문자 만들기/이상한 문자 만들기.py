def solution(s):
    words = s.split(" ") 
    result = [] 
    for word in words:
        new_word = '' 
        for idx, alp in enumerate(word):
            if idx % 2 == 0:
                new_word += alp.upper()
            else:
                new_word += alp.lower()
        result.append(new_word)
    return " ".join(result)