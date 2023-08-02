"""
1. 먼저 행을 돌면서 최대값 갱신하고
2. 다음으로 열을 돌면서 최대값 갱신하고
3. 왼오 대각선 돌면서 최대값 갱신하고
4. 오왼 대각선 돌면서 최대값 갱신하고
5. 젤 큰걸 출력한다.
"""


T = 10
for tc in range(1, T+1):
    test_case = int(input())
    arr = []
    result_of_sum = 0
    max_result = 0
    for _ in range(100):
        arr.append(list(map(int, input().split())))

    # 1. 먼저 행을 돌면서 최대값 갱신하고
    for r in range(100):
        row_temp_result = 0
        for c in range(100):
            row_temp_result += arr[r][c]
            if row_temp_result > max_result:
                max_result = row_temp_result

    # 2. 다음으로 열을 돌면서 최대값 갱신하고
    for c in range(100):
        col_temp_result = 0
        for r in range(100):
            col_temp_result += arr[r][c]
            if col_temp_result > max_result:
                max_result = col_temp_result

    # 3. 왼오 대각선 돌면서 최대값 갱신하고
    left_temp_result = 0
    for c in range(100):
        left_temp_result += arr[c][c]
        if left_temp_result > max_result:
            max_result = left_temp_result

    # 4. 오왼 대각선 돌면서 최대값 갱신하고
    right_temp_result = 0
    for c in range(100):
        right_temp_result += arr[99-c][c]
        if right_temp_result > max_result:
            max_result = right_temp_result

    print(f'#{tc} {max_result}')