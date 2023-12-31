n = int(input())
numlist = list(map(int, input().split()))
orderdict = {num:i for i, num in enumerate(sorted(set(numlist)))}
print(" ".join([str(orderdict[num]) for num in numlist]))