"""
1. 2차원 배열로 바둑판을 만들어서
2. 흑돌은 1, 백돌은 2로 표시해서 두고
3. 돌을 둘때마다 위, 아래, 대각선에 있는 내 돌을 만날때까지, 상대 돌밖에 없다면 다 바꿔주고
4. 비어있거나, 내 돌이 나오기 전에 비면 stop
5. 게임 끝난 후 백돌과 흑돌 개수 세서 출력하자
"""
# 한턴 함수 만들어주기
def one_turn(r, c, color):
    # 위아래, 양옆, 대각선으로 탐색하면서,
    # 위 탐색
    first_r = r
    first_c = c
    temp = []
    is_up = False
    while not is_up:
        # 바둑판을 나가거나, 비어있지 않다면
        if r - 1 >= 0 and arr[r - 1][c] != 0:
            # 이동
            r -= 1
            # 상대 돌이 나오면 저장
            if arr[r][c] != color:
                temp.append([r, c])
            # 내 돌이 나오면 저장된 상대 돌을 전부 바꿔주고 끝내기
            elif arr[r][c] == color:
                for t in range(len(temp)):
                    t_r, t_c = temp[t][0], temp[t][1]
                    arr[t_r][t_c] = color
                is_up = True
                break
        # 만약 비면, 바로 끝내기
        else:
            is_up = True
            break
    # 아래 탐색
    r = first_r
    c = first_c
    temp = []
    is_down = False
    while not is_down:
        # 바둑판을 나가거나, 비어있지 않다면
        if r + 1 < N and arr[r + 1][c] != 0:
            # 이동
            r += 1
            # 상대 돌이 나오면 저장
            if arr[r][c] != color:
                temp.append([r, c])
            # 내 돌이 나오면 저장된 상대 돌을 전부 바꿔주고 끝내기
            elif arr[r][c] == color:
                for t in range(len(temp)):
                    t_r, t_c = temp[t][0], temp[t][1]
                    arr[t_r][t_c] = color
                is_down = True
                break
        # 만약 비면, 바로 끝내기
        else:
            is_down = True
            break
    # 왼쪽 탐색
    r = first_r
    c = first_c
    temp = []
    is_left = False
    while not is_left:
        # 바둑판을 나가거나, 비어있지 않다면
        if c - 1 >= 0 and arr[r][c - 1] != 0:
            # 이동
            c -= 1
            # 상대 돌이 나오면 저장
            if arr[r][c] != color:
                temp.append([r, c])
            # 내 돌이 나오면 저장된 상대 돌을 전부 바꿔주고 끝내기
            elif arr[r][c] == color:
                for t in range(len(temp)):
                    t_r, t_c = temp[t][0], temp[t][1]
                    arr[t_r][t_c] = color
                is_left = True
                break
        # 만약 비면, 바로 끝내기
        else:
            is_left = True
            break
    # 오른쪽 탐색
    r = first_r
    c = first_c
    temp = []
    is_right = False
    while not is_right:
        # 바둑판을 나가거나, 비어있지 않다면
        if c + 1 < N and arr[r][c + 1] != 0:
            # 이동
            c += 1
            # 상대 돌이 나오면 저장
            if arr[r][c] != color:
                temp.append([r, c])
            # 내 돌이 나오면 저장된 상대 돌을 전부 바꿔주고 끝내기
            elif arr[r][c] == color:
                for t in range(len(temp)):
                    t_r, t_c = temp[t][0], temp[t][1]
                    arr[t_r][t_c] = color
                is_right = True
                break
        # 만약 비면, 바로 끝내기
        else:
            is_right = True
            break
    # 왼쪽 위 대각선 탐색
    r = first_r
    c = first_c
    temp = []
    is_left_up = False
    while not is_left_up:
        # 바둑판을 나가거나, 비어있지 않다면
        if r - 1 >= 0 and c - 1 >= 0 and arr[r - 1][c - 1] != 0:
            # 이동
            r -= 1
            c -= 1
            # 상대 돌이 나오면 저장
            if arr[r][c] != color:
                temp.append([r, c])
            # 내 돌이 나오면 저장된 상대 돌을 전부 바꿔주고 끝내기
            elif arr[r][c] == color:
                for t in range(len(temp)):
                    t_r, t_c = temp[t][0], temp[t][1]
                    arr[t_r][t_c] = color
                is_left_up = True
                break
        # 만약 비면, 바로 끝내기
        else:
            is_left_up = True
            break
    # 왼쪽 아래 대각선 탐색
    r = first_r
    c = first_c
    temp = []
    is_left_down = False
    while not is_left_down:
        # 바둑판을 나가거나, 비어있지 않다면
        if r + 1 < N and c - 1 >= 0 and arr[r + 1][c - 1] != 0:
            # 이동
            r += 1
            c -= 1
            # 상대 돌이 나오면 저장
            if arr[r][c] != color:
                temp.append([r, c])
            # 내 돌이 나오면 저장된 상대 돌을 전부 바꿔주고 끝내기
            elif arr[r][c] == color:
                for t in range(len(temp)):
                    t_r, t_c = temp[t][0], temp[t][1]
                    arr[t_r][t_c] = color
                is_left_down = True
                break
        # 만약 비면, 바로 끝내기
        else:
            is_left_down = True
            break
    # 오른쪽 위 대각선 탐색
    r = first_r
    c = first_c
    temp = []
    is_right_up = False
    while not is_right_up:
        # 바둑판을 나가거나, 비어있지 않다면
        if r - 1 >= 0 and c + 1 < N and arr[r - 1][c + 1] != 0:
            # 이동
            r -= 1
            c += 1
            # 상대 돌이 나오면 저장
            if arr[r][c] != color:
                temp.append([r, c])
            # 내 돌이 나오면 저장된 상대 돌을 전부 바꿔주고 끝내기
            elif arr[r][c] == color:
                for t in range(len(temp)):
                    t_r, t_c = temp[t][0], temp[t][1]
                    arr[t_r][t_c] = color
                is_right_up = True
                break
        # 만약 비면, 바로 끝내기
        else:
            is_right_up = True
            break
    # 오른쪽 아래 대각선 탐색
    r = first_r
    c = first_c
    temp = []
    is_right_down = False
    while not is_right_down:
        # 바둑판을 나가거나, 비어있지 않다면
        if r + 1 < N and c + 1 < N and arr[r + 1][c + 1] != 0:
            # 이동
            r += 1
            c += 1
            # 상대 돌이 나오면 저장
            if arr[r][c] != color:
                temp.append([r, c])
            # 내 돌이 나오면 저장된 상대 돌을 전부 바꿔주고 끝내기
            elif arr[r][c] == color:
                for t in range(len(temp)):
                    t_r, t_c = temp[t][0], temp[t][1]
                    arr[t_r][t_c] = color
                is_right_down = True
                break
        # 만약 비면, 바로 끝내기
        else:
            is_right_down = True
            break


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # 1. 2차원 배열로 바둑판을 만들어서
    arr = [[0] * N for _ in range(N)]
    # 4, 6, 8일때 기본 돌 놓기
    if N == 4:
        arr[1][1] = 2
        arr[1][2] = 1
        arr[2][1] = 1
        arr[2][2] = 2
    elif N == 6:
        arr[2][2] = 2
        arr[2][3] = 1
        arr[3][2] = 1
        arr[3][3] = 2
    elif N == 8:
        arr[3][3] = 2
        arr[3][4] = 1
        arr[4][3] = 1
        arr[4][4] = 2

    for _ in range(M):
        r, c, color = map(int, input().split()) # 흑돌은 1, 백돌은 2
        r -= 1
        c -= 1
        # 3. 돌을 둘때마다 위, 아래, 대각선에 있는 내 돌을 만날때까지, 상대 돌밖에 없다면 다 바꿔주고
        # 돌 두기
        arr[r][c] = color
        one_turn(r, c, color)

    result_black = 0
    result_white = 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 1:
                result_black += 1
            elif arr[r][c] == 2:
                result_white += 1

    print(f'#{tc} {result_black} {result_white}')
