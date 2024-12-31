def get_blank(arr: list) -> list:
    temp_blank = []
    for r in range(9):
        for c in range(9):
            if arr[r][c] == 0:
                temp_blank.append([r, c])
    return temp_blank


def check_row(r, num, arr):
    for c in range(9):
        if arr[r][c] == num:
            return False
    return True


def check_col(c, num, arr):
    for r in range(9):
        if arr[r][c] == num:
            return False
    return True


def check_box(r, c, num, arr):
    r = (r // 3) * 3
    c = (c // 3) * 3
    for n in range(3):
        for m in range(3):
            if arr[r + n][c + m] == num:
                return False
    return True


def solution(arr: list, blk: list, now: int):
    if now == len(blk):
        for i in range(9):
            print(*arr[i])
        exit(0)

    for num in range(1, 10):
        r, c = blk[now]
        if check_row(r, num, arr) and check_col(c, num, arr) and check_box(r, c, num, arr):
            arr[r][c] = num
            solution(arr, blk, now + 1)
            arr[r][c] = 0


import sys
input = sys.stdin.readline

array = [list(map(int, input().rstrip().split())) for _ in range(9)]
blank = get_blank(array)
solution(array, blank, 0)