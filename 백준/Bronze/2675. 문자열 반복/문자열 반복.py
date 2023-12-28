N = int(input())

for i in range(N):
    i, S = input().split()
    for j in S:
        print(j*int(i),end="")
    print()