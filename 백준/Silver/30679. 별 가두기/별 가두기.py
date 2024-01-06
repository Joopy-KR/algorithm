import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]


def solve(r, c):
    visited = [[[] for _ in range(M)] for _ in range(N)]
    visited[r][c].append(4)

    direction = 0
    while True:
        # 처음이라면 적힌 방향만큼 오른쪽으로 가기
        if direction == 0:
            if 0 <= c + arr[r][c] < M:
                c += arr[r][c]
                # 만약 사이클이 발생했다면, true 반환
                if 1 in visited[r][c]:
                    return True
                visited[r][c].append(1)
                direction = 1
            # 범위를 나간다면 false 반환
            else:
                return False
        # 오른쪽에서 왔다면, 아래로 가기
        elif direction == 1:
            if 0 <= r + arr[r][c] < N:
                r += arr[r][c]
                # 만약 사이클이 발생했다면, true 반환
                if 2 in visited[r][c]:
                    return True
                visited[r][c].append(2)
                direction = 2
            # 범위를 나간다면 false 반환
            else:
                return False
        # 아래에서 왔다면, 왼쪽으로 가기
        elif direction == 2:
            if 0 <= c - arr[r][c] < M:
                c -= arr[r][c]
                # 만약 사이클이 발생했다면, true 반환
                if 3 in visited[r][c]:
                    return True
                visited[r][c].append(3)
                direction = 3
            # 범위를 나간다면 false 반환
            else:
                return False
        # 왼쪽에서 왔다면, 위로 가기
        elif direction == 3:
            if 0 <= r - arr[r][c] < N:
                r -= arr[r][c]
                # 만약 사이클이 발생했다면, true 반환
                if 4 in visited[r][c]:
                    return True
                visited[r][c].append(4)
                direction = 0
            # 범위를 나간다면 false 반환
            else:
                return False


result = []
for r in range(N):
    if solve(r, 0):
        result.append(r + 1)


print(len(result))
if result:
    print(*result)
