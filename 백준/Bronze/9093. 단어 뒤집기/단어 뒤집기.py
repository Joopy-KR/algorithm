T = int(input())
for tc in range(1, T + 1):
    arr = list(input().split())

    for s in arr:
        print(s[::-1], end=' ')
