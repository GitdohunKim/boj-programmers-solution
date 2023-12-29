n = int(input())
arr = []

for _ in range(n):
    [age, name] = map(str, input().split())
    arr.append([age, name])

arr = sorted(arr, key=lambda x: int(x[0]))

for age, name in arr:
    print(age, name)
