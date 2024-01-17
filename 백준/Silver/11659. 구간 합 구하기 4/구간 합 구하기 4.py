import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [0] + list(map(int, input().split()))

for i in range(1, N + 1):
    arr[i] = arr[i] + arr[i - 1]

for _ in range(M):
    i, j = map(int, input().split())

    print(arr[j] - arr[i - 1])
