"""
1. 행렬을 돌다가 하나라도 색깔이 다른 종이가 나오면
2. start랑 end를 쪼갠다
3. 만약 전부다 같은 색깔이 종이가 나온다면, 해당 색깔 += 1 해준다


"""
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
white = 0
blue = 0

result = []

# 분할정복으로 각각 색종이가 모두 같은 색으로 칠해져 있을때까지 쪼갠다
def divide(x, y, N):
    global white
    global blue
    # 1. 행렬을 돌다가 하나라도 색깔이 다른 종이가 나오면
    for r in range(x, x + N):
        for c in range(y, y + N):
            if arr[x][y] != arr[r][c]:
                # 1사분면
                divide(x, y, N//2)
                # 2사분면
                divide(x, y + N // 2, N // 2)
                # 3사분면
                divide(x + N // 2, y, N // 2)
                # 4사분면
                divide(x + N // 2, y + N // 2, N // 2)
                return

    # 3. 만약 전부다 같은 색깔이 종이가 나온다면, 해당 색깔 += 1 해준다
    if arr[x][y] == 0:
        white += 1
    else:
        blue += 1


divide(0, 0, N)
print(white)
print(blue)