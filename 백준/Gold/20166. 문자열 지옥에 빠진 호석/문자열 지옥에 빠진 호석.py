"""
1. 델타 탐색(8방향) 으로 돌면서
2. 최대 길이 문자열만큼 DFS로 돌면서
3. 신이 좋아하는 문자열(gls)에 있는지 확인한다
4. 단, 이미 왔던 길을 다시 갈 수 있으므로 visited는 쓰지 않는다.
"""
import sys
sys.setrecursionlimit(150000)
input = sys.stdin.readline


# N, M: 격자의 크기 / K: 문자열 개수
N, M, K = map(int, input().rstrip().split())

arr = [list(map(str, input().rstrip())) for _ in range(N)]

gods_love_dict = {}
gods_love_lst = []

for _ in range(K):
    gods_love_str = input().rstrip()
    gods_love_dict[gods_love_str] = 0
    gods_love_lst.append(gods_love_str)


# 델타 탐색 (8방향)
d_r = [-1, -1, 0, 1, 1, 1, 0, -1]
d_c = [0, 1, 1, 1, 0, -1, -1, -1]


def dfs(r, c, cnt, string):
    # 시작하기 전에 이미 문자열의 길이가 최대 길이에 도달했다면
    if cnt == 5:
        return

    # 좋아하는 문자열 목록에 있는지 확인해주기
    if string in gods_love_dict:
        gods_love_dict[string] += 1

    # 1. 델타 탐색(8방향) 으로 돌면서
    for i in range(8):
        nr = r + d_r[i]
        nc = c + d_c[i]
        # 범위 환형 기준으로 재설정 해주기 (어차피 반대쪽 끝, 위아래 끝으로 보내면 그게 대각선이다. 대각선 고려하지 말자)
        # r이 0보다 작다면
        if nr < 0:
            # 아래로 끝까지 보내버리기
            nr += N
        # r이 N - 1보다 크다면
        elif nr > N - 1:
            # 위 끝까지 보내버리기
            nr -= N
        # c가 0보다 작다면
        if nc < 0:
            # 오른쪽 끝까지 보내버리기
            nc += M
        # c가 M - 1보다 크다면
        elif nc > M - 1:
            # 왼쪽 끝까지 보내버리기
            nc -= M

        # 재귀 돌리기
        dfs(nr, nc, cnt + 1, string + arr[nr][nc])


for r in range(N):
    for c in range(M):
        temp = ''
        dfs(r, c, 1, temp + arr[r][c])


for key in gods_love_lst:
    if key in gods_love_dict:
        print(gods_love_dict[key])
