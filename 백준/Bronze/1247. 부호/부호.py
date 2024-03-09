import sys
input = sys.stdin.readline

for tc in range(3):
    N = int(input().rstrip())
    total = 0
    for _ in range(N):
        number = int(input().rstrip())
        total += number
    if total > 0:
        print('+')
    elif total == 0:
        print('0')
    else:
        print('-')
