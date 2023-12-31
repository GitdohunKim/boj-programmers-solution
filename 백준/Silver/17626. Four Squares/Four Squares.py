n=int(input())

while n%4==0:
    n/=4
    
if n%8==7:
    print(4)
else:
    for i in range(1,int(n**0.5)+1):
        if i*i==n:
            print(1)
            break
    else:
        for i in range(int(n**0.5)+1):
            j=int((n-i*i)**0.5)
            if i*i+j*j==n:
                print(2)
                break
        else:
            print(3)



