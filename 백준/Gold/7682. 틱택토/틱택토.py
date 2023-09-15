"""
1. 일단 개수가 맞야함. 번갈아서 놓기 때문에 개수차이는 항상 0 아니면 1임
2. 그리고 항상 X가 1이 많거나 같음. X가 먼저 놓기 때문
3. 만약 빈 공간이 있다면 최종상태인지 검사해야함 최종상태란
3-1. 게임판이 꽉 찼는기
3-2. 아니라면, 어느 한쪽이 이겼는가 (가로, 세로, 대각선으로 같은가)
"""
import sys
input = sys.stdin.readline

end = ['e', 'n', 'd']
while True:
    arr = list(map(str, input().rstrip()))
    if arr == end:
        break
    else:
        # 1. 일단 개수가 맞야함. 번갈아서 놓기 때문에 개수차이는 항상 0 아니면 1임
        x_cnt = 0
        o_cnt = 0
        dot_cnt = 0
        for i in range(9):
            if arr[i] == 'X':
                x_cnt += 1
            elif arr[i] == 'O':
                o_cnt += 1
            else:
                dot_cnt += 1
        # 2. 그리고 항상 X가 1이 많거나 같음. X가 먼저 놓기 때문

        # x가 한개 더 많을때 - 이기면 반드시 x가 이겨야함
        if x_cnt - o_cnt == 1:
            # 3. 만약 빈 공간이 있다면 최종상태인지 검사해야함 최종상태란
            # 3-1. 게임판이 꽉 찼는가 / 어느 한쪽이 이기지 않더라도 valid 함
            # 다만, 두번 이기면 안됨. 첫번째 이겼을때 끝났어야 했으니까
            # 두번 이기더라도, 만약 겹쳐서 이기면 가능함...!
            if not dot_cnt:
                x_bingo = 0
                o_bingo = 0
                total_bingo = 0
                test = [0] * 9
                # 가로 검사
                for r in range(0, 9, 3):
                    if arr[r] == arr[r + 1] == arr[r + 2] and arr[r] != '.':
                        test[r] = test[r + 1] = test[r + 2] = 1
                        total_bingo += 1
                        if arr[r] == 'X':
                            x_bingo += 1
                        else:
                            o_bingo += 1
                # 세로 검사
                for c in range(3):
                    if arr[c] == arr[c + 3] == arr[c + 6] and arr[c] != '.':
                        test[c] = test[c + 3] = test[c + 6] = 1
                        total_bingo += 1
                        if arr[c] == 'X':
                            x_bingo += 1
                        else:
                            o_bingo += 1
                # 대각선 검사
                if arr[0] == arr[4] == arr[8] and arr[0] != '.':
                    test[0] = test[4] = test[8] = 1
                    total_bingo += 1
                    if arr[0] == 'X':
                        x_bingo += 1
                    else:
                        o_bingo += 1
                if arr[2] == arr[4] == arr[6] and arr[2] != '.':
                    test[2] = test[4] = test[6] = 1
                    total_bingo += 1
                    if arr[2] == 'X':
                        x_bingo += 1
                    else:
                        o_bingo += 1
                # 결과 계산
                if o_bingo == 0:
                    if total_bingo == 2:
                        one_cnt = 0
                        for t in test:
                            if t == 1:
                                one_cnt += 1
                        if one_cnt == 5:
                            print("valid")
                            continue
                        else:
                            print("invalid")
                            continue
                    elif total_bingo > 2:
                        print("invalid")
                        continue
                    else:
                        print("valid")
                        continue
                else:
                    print("invalid")
                    continue

            # 3-2. 아니라면, 어느 한쪽이 이겼는가 (가로, 세로, 대각선으로 같은가)
            # 어느 한쪽이 이긴 상태가 아니라면, invalid 함
            # 3-3. 다만, 두번 이기면 안됨. 첫번째 이겼을때 끝났어야 했으니까
            # 두번 이기더라도 만약 겹쳐서 이기면 가능함..!
            else:
                o_bingo = 0
                bingo = 0
                test = [0] * 9
                # 가로 검사
                for r in range(0, 9, 3):
                    if arr[r] == arr[r + 1] == arr[r + 2] and arr[r] != '.':
                        test[r] = test[r + 1] = test[r + 2] = 1
                        bingo += 1
                        if arr[r] == 'O':
                            o_bingo += 1
                # 세로 검사
                for c in range(3):
                    if arr[c] == arr[c + 3] == arr[c + 6] and arr[c] != '.':
                        test[c] = test[c + 3] = test[c + 6] = 1
                        bingo += 1
                        if arr[c] == 'O':
                            o_bingo += 1
                # 대각선 검사
                if arr[0] == arr[4] == arr[8] and arr[0] != '.':
                    test[0] = test[4] = test[8] = 1
                    bingo += 1
                    if arr[0] == 'O':
                        o_bingo += 1
                if arr[2] == arr[4] == arr[6] and arr[2] != '.':
                    test[2] = test[4] = test[6] = 1
                    if arr[2] == 'O':
                        o_bingo += 1
                    bingo += 1

                if o_bingo == 0:
                    if bingo == 1:
                        print("valid")
                        continue
                    elif bingo == 2:
                        one_cnt = 0
                        for t in test:
                            if t == 1:
                                one_cnt += 1
                        if one_cnt == 5:
                            print("valid")
                            continue
                        else:
                            print("invalid")
                            continue
                    elif bingo > 2:
                        print("invalid")
                        continue
                    else:
                        print("invalid")
                        continue
                else:
                    print("invalid")
                    continue

        # 두 개수가 같을때 (반드시 O가 이겨야함..! X는 턴이 끝났으므로)
        elif x_cnt - o_cnt == 0:
            # 3. 만약 빈 공간이 있다면 최종상태인지 검사해야함 최종상태란
            # 3-1. 게임판이 꽉 찼는가 / 어느 한쪽이 이기지 않더라도 valid 함
            # 다만, 두번 이기면 안됨. 첫번째 이겼을때 끝났어야 했으니까
            # 두번 이기더라도, 만약 겹쳐서 이기면 가능함...!
            if not dot_cnt:
                x_bingo = 0
                bingo = 0
                test = [0] * 9
                # 가로 검사
                for r in range(0, 9, 3):
                    if arr[r] == arr[r + 1] == arr[r + 2] and arr[r] != '.':
                        test[r] = test[r + 1] = test[r + 2] = 1
                        bingo += 1
                        if arr[r] == 'X':
                            x_bingo += 1
                # 세로 검사
                for c in range(3):
                    if arr[c] == arr[c + 3] == arr[c + 6] and arr[c] != '.':
                        test[c] = test[c + 3] = test[c + 6] = 1
                        bingo += 1
                        if arr[c] == 'X':
                            x_bingo += 1
                # 대각선 검사
                if arr[0] == arr[4] == arr[8] and arr[0] != '.':
                    test[0] = test[4] = test[8] = 1
                    bingo += 1
                    if arr[0] == 'X':
                        x_bingo += 1
                if arr[2] == arr[4] == arr[6] and arr[2] != '.':
                    test[2] = test[4] = test[6] = 1
                    bingo += 1
                    if arr[2] == 'X':
                        x_bingo += 1
                if x_bingo == 0:
                    if bingo == 2:
                        one_cnt = 0
                        for t in test:
                            if t == 1:
                                one_cnt += 1
                        if one_cnt == 5:
                            print("valid")
                            continue
                        else:
                            print("invalid")
                            continue
                    elif bingo > 2:
                        print("invalid")
                        continue
                    else:
                        print("valid")
                        continue
                else:
                    print("invalid")
                    continue
            # 3-2. 아니라면, 어느 한쪽이 이겼는가 (가로, 세로, 대각선으로 같은가)
            # 어느 한쪽이 이긴 상태가 아니라면, invalid 함
            # 3-3. 다만, 두번 이기면 안됨. 첫번째 이겼을때 끝났어야 했으니까
            # 두번 이기더라도 만약 겹쳐서 이기면 가능함..!
            else:
                x_bingo = 0
                bingo = 0
                test = [0] * 9
                # 가로 검사
                for r in range(0, 9, 3):
                    if arr[r] == arr[r + 1] == arr[r + 2] and arr[r] != '.':
                        test[r] = test[r + 1] = test[r + 2] = 1
                        bingo += 1
                        if arr[r] == 'X':
                            x_bingo += 1

                # 세로 검사
                for c in range(3):
                    if arr[c] == arr[c + 3] == arr[c + 6] and arr[c] != '.':
                        test[c] = test[c + 3] = test[c + 6] = 1
                        bingo += 1
                        if arr[c] == 'X':
                            x_bingo += 1
                # 대각선 검사
                if arr[0] == arr[4] == arr[8] and arr[0] != '.':
                    test[0] = test[4] = test[8] = 1
                    bingo += 1
                    if arr[0] == 'X':
                        x_bingo += 1
                if arr[2] == arr[4] == arr[6] and arr[2] != '.':
                    test[2] = test[4] = test[6] = 1
                    bingo += 1
                    if arr[2] == 'X':
                        x_bingo += 1

                if x_bingo == 0:
                    if bingo == 1:
                        print("valid")
                        continue
                    elif bingo == 2:
                        one_cnt = 0
                        for t in test:
                            if t == 1:
                                one_cnt += 1
                        if one_cnt == 5:
                            print("valid")
                            continue
                        else:
                            print("invalid")
                            continue
                    elif bingo > 2:
                        print("invalid")
                        continue
                    else:
                        print("invalid")
                        continue
                else:
                    print("invalid")
                    continue
        else:
            print("invalid")
            continue
