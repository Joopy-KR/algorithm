import sys
input = sys.stdin.readline


def solution(n, arr, poss, now):
    global result
    if now == n:
        result += 1
        return
    for i in range(n):
        if poss[now][i] < 1:
            continue
        arr[now][i] = True  # 현재 위치 True
        # 세로 비활성화
        for r in range(now + 1, n):
            poss[r][i] -= 1
        # 왼쪽 대각선 비활성화
        r_idx = now
        c_idx = i
        for j in range(now + 1, n):
            r_idx += 1
            c_idx -= 1
            if 0 <= r_idx < n and 0 <= c_idx < n:
                poss[r_idx][c_idx] -= 1
        # 오른쪽 대각선 비활성화
        r_idx = now
        c_idx = i
        for k in range(now + 1, n):
            r_idx += 1
            c_idx += 1
            if 0 <= r_idx < n and 0 <= c_idx < n:
                poss[r_idx][c_idx] -= 1

        # 다음꺼 갔다오기
        solution(n, arr, poss, now + 1)
        # 현재 위치 비활성화
        arr[now][i] = False

        # 세로 활성화
        for r in range(now + 1, n):
            poss[r][i] += 1
        # 왼쪽 대각선 활성화
        r_idx = now
        c_idx = i
        for j in range(now + 1, n):
            r_idx += 1
            c_idx -= 1
            if 0 <= r_idx < n and 0 <= c_idx < n:
                poss[r_idx][c_idx] += 1
        # 오른쪽 대각선 비활성화
        r_idx = now
        c_idx = i
        for k in range(now + 1, n):
            r_idx += 1
            c_idx += 1
            if 0 <= r_idx < n and 0 <= c_idx < n:
                poss[r_idx][c_idx] += 1


N = int(input())
possible = [[1] * N for _ in range(N)]
ARR = [[False] * N for _ in range(N)]
result = 0
solution(N, ARR, possible, 0)
print(result)
