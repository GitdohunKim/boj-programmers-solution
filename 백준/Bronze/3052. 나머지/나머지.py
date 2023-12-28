num_list = [int(input()) for i in range(10)] 
for i in range(10):
  num_list[i] = num_list[i] % 42


num_list = set(num_list)
print(len(num_list))