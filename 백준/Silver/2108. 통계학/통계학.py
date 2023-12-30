from collections import Counter
import sys

N = int(sys.stdin.readline())
num_list = [int(sys.stdin.readline()) for _ in range(N)]
sort_num_list = sorted(num_list)

avg = round(sum(num_list) / len(num_list)) 
med = sort_num_list[len(num_list)//2]

freq_dict = dict(Counter(num_list))
max_value = max(freq_dict.values())
freq_candidate = [key for key,value in freq_dict.items() if value == max_value]
if len(freq_candidate) == 1:
    freq = freq_candidate[0]
else:
    freq = sorted(freq_candidate)[1]

rang = sort_num_list[-1] - sort_num_list[0]

print(avg, med, freq, rang, sep = '\n')