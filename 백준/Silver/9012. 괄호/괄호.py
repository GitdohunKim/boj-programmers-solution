T= int(input())

for _ in range(T):
  a = list(map(str,input().rstrip()))
  stack = []

  for elem in a:
    if elem =="(":
      stack.append(elem)
    else :
      if len(stack)==0:
        stack.append(elem)
        break
      else :
        stack.pop()

  if len(stack)==0:
    print("YES")
  else :
    print("NO")