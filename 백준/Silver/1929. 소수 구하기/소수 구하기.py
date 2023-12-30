MAX=1000001
prime_check=[True]*MAX
prime_check[0]=False
prime_check[1]=False
for i in range(2,MAX):
    if prime_check[i]==True:
        for j in range(i+i,MAX,i):
            prime_check[j]=False

n,m=map(int,input().split())
for i in range(n,m+1):
    if prime_check[i]==True:
        print(i)