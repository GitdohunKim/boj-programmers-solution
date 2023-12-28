S = list(input().strip())
positions = [-1] * 26 

for i, char in enumerate(S):
    index = ord(char) - ord('a') 
    if positions[index] == -1:
        positions[index] = i

for pos in positions:
    print(pos, end=' ')
