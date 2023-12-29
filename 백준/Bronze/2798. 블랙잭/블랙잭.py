import sys

cardCount, targetSum = map(int, sys.stdin.readline().strip().split())
cards = list(map(int, sys.stdin.readline().strip().split()))

maxSum = -1

for i in range(cardCount):
    for j in range(i+1,cardCount):
        for k in range(j+1,cardCount):
            tempSum = cards[i] + cards[j] + cards[k]

            if (maxSum <= tempSum and tempSum <= targetSum):
                maxSum = tempSum

    if (maxSum == targetSum):
        break


print(maxSum)    