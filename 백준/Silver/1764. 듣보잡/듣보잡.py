import sys

input = sys.stdin.readline

n, m = map(int,input().split())

noListenPeoples = {}
noSeePeoples = []
for _ in range(n) :
    noListenPeoples[input().strip()] = True

for _ in range(m) :
    noSeePeople = input().strip()

    if noListenPeoples.get(noSeePeople) != None :
        noSeePeoples.append(noSeePeople)

noSeePeoples.sort()
print(len(noSeePeoples))
print(*noSeePeoples, sep="\n")