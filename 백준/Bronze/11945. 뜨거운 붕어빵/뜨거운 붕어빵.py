# N = 행, M = 열

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input())))


for r in range(N):
    for c in range(M//2): # 반만 바꾼다 (다 바꾸면 원상복구이므로)
        arr[r][c], arr[r][M-1-c] = arr[r][M-1-c], arr[r][c]

for i in arr:
    for j in i:
        print(j, end="")
    print("")