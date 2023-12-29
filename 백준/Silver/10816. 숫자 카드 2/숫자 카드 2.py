N = int(input())
deck = list(map(int, input().split()))

M = int(input())
cards = list(map(int, input().split()))

count_deck = dict()

for d in deck:
    if d in count_deck:
        count_deck[d] += 1
    else:
        count_deck[d] = 1

for card in cards:

    if card in count_deck:
        print(count_deck[card], end=' ')
    else:
        print(0, end=' ')