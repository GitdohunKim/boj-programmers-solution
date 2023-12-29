n=int(input())
devil=0
cnt=0
while True:
    devil+=1
    if '666' in str(devil):
        cnt+=1
    if cnt==n:
        print(devil)
        break