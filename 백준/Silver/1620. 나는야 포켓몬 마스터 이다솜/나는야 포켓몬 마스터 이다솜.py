import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

arr = [input().rstrip() for _ in range(N)]

for _ in range(M):
    query = input().rstrip()

    if query.isdigit():
        print(arr[int(query) - 1])

    else:
        print(arr.index(query) + 1)