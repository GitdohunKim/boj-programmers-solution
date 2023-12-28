word=str(input()).lower()
word_list=list(set(word))
a=[]
for i in word_list:
    count=word.count(i)
    a.append(count)
    
if a.count(max(a))>=2:
    print("?")
    
else:
    print(word_list[a.index(max(a))].upper())
