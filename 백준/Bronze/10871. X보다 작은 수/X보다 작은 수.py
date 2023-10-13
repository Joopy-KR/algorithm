N, X = map(int, input().split())
arr = list(map(int, input().split()))
result = []

for a in arr:
    if a < X:
        print(a, end=' ')
        