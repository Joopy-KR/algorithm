import sys
input = sys.stdin.readline

T = int(input().rstrip())

for tc in range(1, T + 1):
    N = int(input())
    X = list(map(int, input().split()))

    for i in range(1, N):
        X[i] = max(X[i], X[i] + X[i - 1])

    print(max(X))