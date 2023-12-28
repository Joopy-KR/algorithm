"""
1. 행열을 한번 돌면서 확산이 일어나야하는 칸과, 그 값을 기록해둔다 (공기청정기 값도 기록)
2. 기록해둔 값을 토대로 확산을 돌면서 값을 변화시킨다
3. 공기청정기 위치를 윗공기청정기와 아래 공기청정기로 나눈 후 값을 변화시켜준다
4. T초가 경과했다면 값을 출력한다
"""
import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(R)]

while T > 0:
    T -= 1
    # 1. 행열을 한번 돌면서 확산이 일어나야하는 칸과, 그 값을 기록해둔다 (공기청정기 값도 기록)
    dusts = []
    air_cleaner = []
    for r in range(R):
        for c in range(C):
            # 확산이 일어나야 하는 칸이라면
            if arr[r][c] > 0:
                # r, c, //5 한 값 순서대로 기록하기
                dusts.append([r, c, arr[r][c] // 5])
            # 공기청정기가 있다면
            if arr[r][c] == -1:
                # 기록해두기 (먼저 기록된기 윗 공기청정기, 어차피 1열이므로 행만기록)
                air_cleaner.append([r, c])

    # 2. 기록해둔 값을 토대로 확산을 돌면서 값을 변화시킨다
    # 돌면서 //5 한 값을 더해주고 cnt += 1하기
    # cnt 개수만큼 원래 값에서 빼버리기
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    for dust in dusts:
        cnt = 0
        for i in range(4):
            nr = dust[0] + dr[i]
            nc = dust[1] + dc[i]
            # 옆이 공기청정기라면 확산되지 않음
            if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] != -1:
                cnt += 1
                # 돌면서 //5 한 값을 더해주고 cnt += 1하기
                arr[nr][nc] += dust[2]
        # cnt 개수만큼 원래 값에서 빼버리기
        arr[dust[0]][dust[1]] -= dust[2] * cnt

    # 3. 공기청정기 위치를 윗공기청정기와 아래 공기청정기로 나눈 후 값을 변화시켜준다
    # 윗 공기청정기 (오른쪽으로 이동)
    upper_cleaner = air_cleaner[0].copy()

    # 오른쪽으로 이동
    # 다음번이 남아있다면
    old_val = 0
    new_val = 0
    while upper_cleaner[1] + 1 < C:
        # 다음 단계로 옮긴 다음
        upper_cleaner[1] += 1
        # 첫번째 경우 관리
        if upper_cleaner[1] == 1:
            old_val = arr[upper_cleaner[0]][upper_cleaner[1]]
            arr[upper_cleaner[0]][upper_cleaner[1]] = 0
            continue

        # 이동할 자리에 있던 먼지 값을 기록
        new_val = arr[upper_cleaner[0]][upper_cleaner[1]]

        # 현재 자리에 왼쪽 값을 옮김
        arr[upper_cleaner[0]][upper_cleaner[1]] = old_val

        # 값 스위칭
        old_val = new_val

    # 위로 이동
    while 0 <= upper_cleaner[0] - 1:
        # 다음 단계로 옮긴 다음
        upper_cleaner[0] -= 1

        # 이동할 자리에 있던 먼지 값을 기록
        new_val = arr[upper_cleaner[0]][upper_cleaner[1]]

        # 현재 자리에 왼쪽 값을 옮김
        arr[upper_cleaner[0]][upper_cleaner[1]] = old_val

        # 값 스위칭
        old_val = new_val

    # 왼쪽으로 이동
    while 0 <= upper_cleaner[1] - 1:
        # 다음 단계로 옮긴 다음
        upper_cleaner[1] -= 1

        # 이동할 자리에 있던 먼지 값을 기록
        new_val = arr[upper_cleaner[0]][upper_cleaner[1]]

        # 현재 자리에 왼쪽 값을 옮김
        arr[upper_cleaner[0]][upper_cleaner[1]] = old_val

        # 값 스위칭
        old_val = new_val

    # 아래로 이동
    while True:
        # 다음 단계로 옮긴 다음
        upper_cleaner[0] += 1

        # 마지막 경우 관리
        if arr[upper_cleaner[0]][upper_cleaner[1]] == -1:
            break
        else:
            # 이동할 자리에 있던 먼지 값을 기록
            new_val = arr[upper_cleaner[0]][upper_cleaner[1]]

            # 현재 자리에 왼쪽 값을 옮김
            arr[upper_cleaner[0]][upper_cleaner[1]] = old_val

            # 값 스위칭
            old_val = new_val


    # 아래 공기청정기 (오른쪽으로 이동)
    upper_cleaner = air_cleaner[1].copy()

    # 오른쪽으로 이동
    # 다음번이 남아있다면
    old_val = 0
    new_val = 0
    while upper_cleaner[1] + 1 < C:
        # 다음 단계로 옮긴 다음
        upper_cleaner[1] += 1
        # 첫번째 경우 관리
        if upper_cleaner[1] == 1:
            old_val = arr[upper_cleaner[0]][upper_cleaner[1]]
            arr[upper_cleaner[0]][upper_cleaner[1]] = 0
            continue

        # 이동할 자리에 있던 먼지 값을 기록
        new_val = arr[upper_cleaner[0]][upper_cleaner[1]]

        # 현재 자리에 왼쪽 값을 옮김
        arr[upper_cleaner[0]][upper_cleaner[1]] = old_val

        # 값 스위칭
        old_val = new_val

    # 아래로 이동
    while upper_cleaner[0] + 1 < R:
        # 다음 단계로 옮긴 다음
        upper_cleaner[0] += 1

        # 이동할 자리에 있던 먼지 값을 기록
        new_val = arr[upper_cleaner[0]][upper_cleaner[1]]

        # 현재 자리에 왼쪽 값을 옮김
        arr[upper_cleaner[0]][upper_cleaner[1]] = old_val

        # 값 스위칭
        old_val = new_val

    # 왼쪽으로 이동
    while 0 <= upper_cleaner[1] - 1:
        # 다음 단계로 옮긴 다음
        upper_cleaner[1] -= 1

        # 이동할 자리에 있던 먼지 값을 기록
        new_val = arr[upper_cleaner[0]][upper_cleaner[1]]

        # 현재 자리에 왼쪽 값을 옮김
        arr[upper_cleaner[0]][upper_cleaner[1]] = old_val

        # 값 스위칭
        old_val = new_val

    # 위로 이동
    while True:
        # 다음 단계로 옮긴 다음
        upper_cleaner[0] -= 1

        # 마지막 경우 관리
        if arr[upper_cleaner[0]][upper_cleaner[1]] == -1:
            break
        else:
            # 이동할 자리에 있던 먼지 값을 기록
            new_val = arr[upper_cleaner[0]][upper_cleaner[1]]

            # 현재 자리에 왼쪽 값을 옮김
            arr[upper_cleaner[0]][upper_cleaner[1]] = old_val

            # 값 스위칭
            old_val = new_val

result = 0
# 계산하기
for r in range(R):
    for c in range(C):
        if arr[r][c] != -1:
            result += arr[r][c]

print(result)