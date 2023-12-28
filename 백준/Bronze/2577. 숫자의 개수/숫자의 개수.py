a=int(input())
b=int(input())
c=int(input())
dict_count = {i: 0 for i in range(10)}

num_product = a * b * c
for i in str(num_product):
    dict_count[int(i)] += 1

for i in dict_count.keys():
    print(dict_count[i])
