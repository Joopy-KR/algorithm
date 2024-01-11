import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

T = int(input().rstrip())
for tc in range(1, T + 1):
    N = int(input().rstrip())
    arr = [0] + list(map(int, input().split()))
    finished = [0] * (N + 1)
    result = []

    def DFS(n):
        global result
        check.append(n)
        finished[n] = 1
        n = arr[n]

        if finished[n]:
            if n in check:
                result += check[check.index(n):]
            return
        else:
            DFS(n)

        # # 만약 다음 방문할 곳이 방문하지 않을 곳이라면
        # if arr[n] not in check:
        #     n = arr[n]
        #     check.append(n)
        #     finished[n] = 1
        #     # 만약 도착한 곳이 번호와 자기가 같은 곳이라면
        #     # 걔를 빼고 나머지 check에 들어있던 친구들은
        #     # 모두 팀이 없는애들. 하나 빼고 나머지 return
        #     if n == arr[n]:
        #         return len(check) - 1
        # # 이미 방문한 곳이라면
        # else:
        #     # 역시 번호가 자기와 같다면 return
        #     if n == arr[n]:
        #         return len(check) - 1
        #
        #     # 그게 아니라 사이클이 생긴거라면
        #     else:
        #         # 사이클이 생긴 곳부터! 세야함(중요)
        #         idx = check.index(arr[n])
        #
        #         return len(check[:idx])

    for i in range(1, N + 1):
        if finished[i] == 0:
            check = []
            DFS(i)

    print(N - len(result))
