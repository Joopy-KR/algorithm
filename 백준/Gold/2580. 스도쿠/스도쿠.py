import sys
input = sys.stdin.readline

arr = [list(map(int, input().rstrip().split())) for _ in range(9)]
blank = []

for n in range(9):
    for m in range(9):
        if arr[n][m] == 0:
            blank.append([n, m])


def is_row(r, num):
    for c in range(9):
        if arr[r][c] == num:
            return False
    return True


def is_col(c, num):
    for r in range(9):
        if arr[r][c] == num:
            return False
    return True


def is_box(r, c, num):
    nr = (r // 3) * 3
    nc = (c // 3) * 3
    for i in range(3):
         for j in range(3):
             if arr[nr + i][nc + j] == num:
                 return False
    return True


def solution(idx):
    if idx == len(blank):
        for i in range(9):
            print(*arr[i])
        exit(0)

    for j in range(1, 10):
        x, y = blank[idx]
        if is_row(x, j) and is_col(y, j) and is_box(x, y, j):
            arr[x][y] = j
            solution(idx + 1)
            arr[x][y] = 0


solution(0)