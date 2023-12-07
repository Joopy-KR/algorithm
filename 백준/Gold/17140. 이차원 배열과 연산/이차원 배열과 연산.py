import sys
input = sys.stdin.readline


r, c, k = map(int, input().rstrip().split())

R = r
C = c

arr = [list(map(int, input().rstrip().split())) for _ in range(3)]

cnt = 0

while cnt <= 100:
    # 만약 인덱스 에러가 아니라면
    try:
        if arr[R - 1][C - 1] == k:
            print(cnt)
            break
        cnt += 1
        temp = []

        # R연산 수행하기 (행의 개수 >= 열의 개수)
        if len(arr) >= len(arr[0]):
            for r in range(len(arr)):
                # 행이 넘어갈때 초기화 시켜주기
                check = [0] * 101
                how_many = []
                for c in range(len(arr[0])):
                    # 개수 세주기
                    check[arr[r][c]] += 1
                # 개수 세기가 끝났다면
                for i in range(101):
                    # 개수가 있다면
                    if check[i] != 0:
                        if i != 0:
                            how_many.append([i, check[i]])

                # 개수별로 정렬하기 (뒤에껄로 먼저 정렬하고, 그 다음 앞에껄로 정렬)
                how_many.sort(key=lambda x: (x[1], x[0]))

                temp.append(how_many)

            max_len = 0

            for ar in temp:
                max_len = max(max_len, len(ar))

            # 하나하나 새롭게 arr 에 집어넣으면서, 만약에 길이가 max_len 보다 짧다면, 0으로 채워버린다
            arr = []
            for i in range(len(temp)):
                if i < 101:
                    arr.append([])
                else:
                    break
                for j in range(max_len):
                    if j < 101:
                        try:
                            arr[i].extend(temp[i][j])
                        except:
                            arr[i].extend([0, 0])
                    else:
                        break

        # C연산 수행하기 (행의 개수 < 열의 개수)
        else:
            for c in range(len(arr[0])):
                # 행이 넘어갈때 초기화 시켜주기
                check = [0] * 101
                how_many = []
                for r in range(len(arr)):
                    # 개수 세주기
                    check[arr[r][c]] += 1
                # 개수 세기가 끝났다면
                for i in range(101):
                    # 개수가 있다면
                    if check[i] != 0:
                        if i != 0:
                            how_many.append([i, check[i]])

                # 개수별로 정렬하기 (뒤에껄로 먼저 정렬하고, 그 다음 앞에껄로 정렬)
                how_many.sort(key=lambda x: (x[1], x[0]))

                temp.append(how_many)

            max_len = 0

            for ar in temp:
                max_len = max(max_len, len(ar))

            if len(temp) > 100:
                temp = temp[:101]

            if max_len > 50:
                max_len = 50

            # 하나하나 새롭게 arr 에 집어넣으면서, 만약에 길이가 max_len 보다 짧다면, 0으로 채워버린다
            arr = [[0] * len(temp) for _ in range(max_len * 2)]

            pre_process = []
            for i in range(len(temp)):
                pre_process.append([])
                for j in range(len(temp[i])):
                    pre_process[i].extend(temp[i][j])
                    if len(pre_process[i]) > 100:
                        pre_process[i] = pre_process[i][:101]

            for c in range(len(temp)):
                for r in range(max_len * 2):
                    try:
                        arr[r][c] = pre_process[c][r]
                    except:
                        pass



    # 인덱스 에러가 났다면
    except:
        cnt += 1
        temp = []

        # R연산 수행하기 (행의 개수 >= 열의 개수)
        if len(arr) >= len(arr[0]):
            for r in range(len(arr)):
                # 행이 넘어갈때 초기화 시켜주기
                check = [0] * 101
                how_many = []
                for c in range(len(arr[0])):
                    # 개수 세주기
                    check[arr[r][c]] += 1
                # 개수 세기가 끝났다면
                for i in range(101):
                    # 개수가 있다면
                    if check[i] != 0:
                        if i != 0:
                            how_many.append([i, check[i]])

                # 개수별로 정렬하기 (뒤에껄로 먼저 정렬하고, 그 다음 앞에껄로 정렬)
                how_many.sort(key=lambda x: (x[1], x[0]))

                temp.append(how_many)

            max_len = 0

            for ar in temp:
                max_len = max(max_len, len(ar))

            # 하나하나 새롭게 arr 에 집어넣으면서, 만약에 길이가 max_len 보다 짧다면, 0으로 채워버린다
            arr = []
            for i in range(len(temp)):
                if i < 101:
                    arr.append([])
                else:
                    break
                for j in range(max_len):
                    if j < 101:
                        try:
                            arr[i].extend(temp[i][j])
                        except:
                            arr[i].extend([0, 0])
                    else:
                        break

        # C연산 수행하기 (행의 개수 < 열의 개수)
        else:
            for c in range(len(arr[0])):
                # 행이 넘어갈때 초기화 시켜주기
                check = [0] * 101
                how_many = []
                for r in range(len(arr)):
                    # 개수 세주기
                    check[arr[r][c]] += 1
                # 개수 세기가 끝났다면
                for i in range(101):
                    # 개수가 있다면
                    if check[i] != 0:
                        if i != 0:
                            how_many.append([i, check[i]])

                # 개수별로 정렬하기 (뒤에껄로 먼저 정렬하고, 그 다음 앞에껄로 정렬)
                how_many.sort(key=lambda x: (x[1], x[0]))

                temp.append(how_many)

            max_len = 0

            for ar in temp:
                max_len = max(max_len, len(ar))

            if len(temp) > 100:
                temp = temp[:101]

            if max_len > 50:
                max_len = 50

            # 하나하나 새롭게 arr 에 집어넣으면서, 만약에 길이가 max_len 보다 짧다면, 0으로 채워버린다
            arr = [[0] * len(temp) for _ in range(max_len * 2)]

            pre_process = []
            for i in range(len(temp)):
                pre_process.append([])
                for j in range(len(temp[i])):
                    pre_process[i].extend(temp[i][j])
                    if len(pre_process[i]) > 100:
                        pre_process[i] = pre_process[i][:101]

            for c in range(len(temp)):
                for r in range(max_len * 2):
                    try:
                        arr[r][c] = pre_process[c][r]
                    except:
                        pass


else:
    print(-1)