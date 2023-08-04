from pprint import pprint as pp

"""
1. 정답지 리스트를 돌면서 빙고판을 돌면서 숫자가 나오면 0으로 바꾸고
2. 그 다음 정답지 리스트를 돌기 전에, 빙고판을 돌면서 가로, 세로, 대각선으로 0이 5개인지 탐색하고
3. 없으면 count 1추가하고 계속하고, 있으면 count를 반환한다. 
"""
arr = []
answer = []
for _ in range(5):
    arr.append(list(map(int, input().split())))
for _ in range(5):
    answer.append(list(map(int, input().split())))

def solve_problem():
    result = 0
    for r in range(5):
        for c in range(5):
            temp = answer[r][c]
            result += 1
            # # 1. 정답지 리스트를 돌면서 빙고판을 돌면서 숫자가 나오면 0으로 바꾸고
            for r1 in range(5):
                for c1 in range(5):
                    if arr[r1][c1] == temp:
                        arr[r1][c1] = 0
    # 2. 그 다음 정답지 리스트를 돌기 전에, 빙고판을 돌면서 가로, 세로, 대각선으로 0이 5개인지 탐색
            # 2-1 가로 탐색
            bingo = 0
            for r2 in range(5):
                temp_row_cnt = 0
                for c2 in range(5):
                    if arr[r2][c2] == 0:
                        temp_row_cnt += 1
                        if temp_row_cnt == 5:
                            bingo += 1
            # 2-2 세로 탐색
            for c3 in range(5):
                temp_col_cnt = 0
                for r3 in range(5):
                    if arr[r3][c3] == 0:
                        temp_col_cnt += 1
                        if temp_col_cnt == 5:
                            bingo += 1
            # 2-3 대각선 탐색
            temp_cross1_cnt = 0
            for c4 in range(5):
                if arr[c4][c4] == 0:
                    temp_cross1_cnt += 1
                    if temp_cross1_cnt == 5:
                        bingo += 1
            temp_cross2_cnt = 0
            for c5 in range(5):
                if arr[c5][4-c5] == 0:
                    temp_cross2_cnt += 1
                    if temp_cross2_cnt == 5:
                        bingo += 1

            if bingo >= 3:
                return result

print(solve_problem())