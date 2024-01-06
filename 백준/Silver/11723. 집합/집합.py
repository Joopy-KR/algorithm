import sys
input = sys.stdin.readline

M = int(input().rstrip())
S = set()
for _ in range(M):
    arr = list(map(str, input().rstrip().split()))

    if arr == ['all']:
        S = set(i for i in range(1, 21))

    elif arr == ['empty']:
        S = set()

    else:
        order, num = arr
        num = int(num)

        if order == 'add':
            S.add(num)
        elif order == 'remove':
            S.discard(num)
        elif order == 'check':
            if num in S:
                print(1)
            else:
                print(0)
        elif order == 'toggle':
            if num in S:
                S.discard(num)
            else:
                S.add(num)
