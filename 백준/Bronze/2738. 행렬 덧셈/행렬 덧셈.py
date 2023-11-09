N, M = map(int, input().split())

arr1 = [list(map(int, input().split())) for _ in range(N)]

arr2 = [list(map(int, input().split())) for _ in range(N)]

arr3 = [[0] * M for _ in range(N)]


for r in range(N):
    for c in range(M):
        arr3[r][c] = arr1[r][c] + arr2[r][c]

for i in arr3:
    print(*i)