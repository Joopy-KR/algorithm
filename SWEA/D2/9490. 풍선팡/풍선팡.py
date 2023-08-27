T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    max_result = 0

    for r in range(N):
        for c in range(M):
            temp_result = 0
            temp_result += arr[r][c]  # 자기 자신 더하기
            for i in range(4):
                for j in range(1, arr[r][c] + 1):
                    nr = r + (dr[i] * j)
                    nc = c + (dc[i] * j)
                    if 0 <= nr < N and 0 <= nc < M:
                        temp_result += arr[nr][nc]
            if temp_result > max_result:
                max_result = temp_result

    print(f'#{tc} {max_result}')
