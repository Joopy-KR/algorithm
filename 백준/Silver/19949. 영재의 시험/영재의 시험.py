import sys
input = sys.stdin.readline

answer = [0] + list(map(int, input().rstrip().split()))
output = [0] * 11
visited = [0] * 6
result = 0
bingo = 0


def solve(cnt):
    global result
    global visited
    global bingo

    if cnt == 11:
        temp = 0
        for j in range(1, 11):
            if output[j] == answer[j]:
                temp += 1
        if temp >= 5:
            result += 1
        return

    # 1번부터 5번까지 번호를 골라줄껀데
    for i in range(1, 6):
        # 만약 연속으로 두번 고른게 아니라면
        if visited[i] != 2:
            # 배열에 해당 숫자 추가
            output[cnt] = i
            # 지금 고른 숫자가 정답이라면
            # if output[cnt] == answer[cnt]:
            #     bingo += 1

            # 5점 이상이라면
            # if bingo >= 5:
            #     result += 1

            # 만약 처음 고르는 숫자라면
            if visited[i] == 0:
                # 배열 초기화(전에 있던거 없애기) 후 1 더해주고
                visited = [0] * 6
                visited[i] += 1
            else:
                # 전에 골랐던 거라면 살포시 하나더 추가
                visited[i] += 1

            cnt += 1
            solve(cnt)
            # 돌아왔을 때 지워주기

            cnt -= 1

            # if output[cnt] == answer[cnt]:
            #     bingo -= 1

            # 내 이전 두 숫자가 남아있다면
            if cnt >= 3:
                visited = [0] * 6
                if output[cnt - 1] == output[cnt - 2]:
                    visited[output[cnt - 1]] += 2
                else:
                    visited[output[cnt - 1]] += 1
            # 내 전에 한 개 남아있다면 (내가 두번째라면)
            elif cnt == 2:
                visited = [0] * 6
                visited[output[cnt - 1]] += 1
            # 내가 첫번째라면
            elif cnt == 1:
                visited = [0] * 6


solve(1)
print(result)