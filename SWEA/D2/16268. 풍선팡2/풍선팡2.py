T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    max_sum = 0

    for r in range(N):
        for c in range(M):
            temp_sum = 0
            temp_sum += arr[r][c]  # 자기 자신 더해주기
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < N and 0 <= nc < M:
                    temp_sum += arr[nr][nc]
            if temp_sum > max_sum:
                max_sum = temp_sum

    print(f'#{tc} {max_sum}')
