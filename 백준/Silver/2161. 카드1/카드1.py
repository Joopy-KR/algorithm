n = int(input())
card = [i for i in range(1, n + 1)]
discard = []
while len(card) != 1:
    discard.append(card.pop(0)) # 제일 위에 있는 카드를 버린다.
    card.append(card.pop(0))    # 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
for c in discard:
    print(c, end=' ')
print(card[0])