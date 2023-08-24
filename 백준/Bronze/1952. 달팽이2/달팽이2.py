import sys
input = sys.stdin.readline

M, N = map(int, input().rstrip().split())
arr = [[0] * N for _ in range(M)]


def snail(arr):
    r = 0
    c = 0
    arr[r][c] = 1
    result = 0
    # 오른쪽으로 가기
    while True:
        is_down = False
        is_left = False
        is_up = False
        # 오른쪽으로 쭉 가다가 범위를 나가거나 1을 만나면
        if c + 1 >= N or arr[r][c + 1] == 1:
            # 아래로 꺾지도 못하면 (탐색이 끝나면) 끝내고
            if r + 1 >= M or arr[r + 1][c] == 1:
                return result
            # 아니면 아래로 꺾는다
            else:
                r += 1
                arr[r][c] = 1
                result += 1
            # 아래로 가기
            while not is_down:
                # 아래로 쭉 가다가 범위를 나가거나 1을 만나면
                if r + 1 >= M or arr[r + 1][c] == 1:
                    # 왼쪽으로 꺾지도 못하면 끝내고
                    if c - 1 < 0 or arr[r][c - 1] == 1:
                        return result
                    # 아니면 왼쪽으로 꺾는다
                    else:
                        c -= 1
                        result += 1
                        arr[r][c] = 1
                        is_down = True
                        # 왼쪽으로 가기
                        while not is_left:
                            # 왼쪽으로 쭉 가다가 범위를 나가거나 1을 만나면
                            if c - 1 < 0 or arr[r][c - 1] == 1:
                                # 위로 꺾지도 못하면 (탐색이 끝나면) 끝내고
                                if r - 1 < 0 or arr[r - 1][c] == 1:
                                    return result
                                # 아니면 위로 꺾는다
                                else:
                                    r -= 1
                                    result += 1
                                    arr[r][c] = 1
                                    is_left = True
                                    # 위로 가기
                                    while not is_up:
                                        # 위로 쭉 가다가 범위를 나가거나 1을 만나면
                                        if r - 1 < 0 or arr[r - 1][c] == 1:
                                            # 오른쪽으로 꺾지도 못하면 끝내고
                                            if c + 1 >= N or arr[r][c + 1] == 1:
                                                return result
                                            # 아니면 오른쪽으로 꺾는다
                                            else:
                                                c += 1
                                                result += 1
                                                arr[r][c] = 1
                                                is_up = True
                                        # 위로 이동
                                        else:
                                            r -= 1
                                            arr[r][c] = 1
                            # 왼쪽으로 이동
                            else:
                                c -= 1
                                arr[r][c] = 1
                # 아래로 이동
                else:
                    r += 1
                    arr[r][c] = 1
        # 오른쪽으로 이동
        else:
            c += 1
            arr[r][c] = 1


print(snail(arr))