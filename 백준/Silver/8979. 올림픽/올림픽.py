import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())

arr = [list(map(int, input().rstrip().split())) for _ in range(N)]
# 1열은 국가 번호, 2열은 금메달, 3열은 은메달, 4열은 동메달

# 금메달 순으로 정렬된 상태
arr.sort(key=lambda x: (-x[1], -x[2], -x[3]))
result = []
temp = []
rank = 1
for i in range(1, N):
    if i != N - 1:
        # 금메달 개수가 같은가
        if arr[i][1] == arr[i - 1][1]:
            # 은메달 개수가 같은가
            if arr[i][2] == arr[i - 1][2]:
                # 동메달 개수가 같은가
                if arr[i][3] == arr[i - 1][3]:
                    # 만약 다 같으면
                    temp.append([arr[i - 1][0], rank])
                else:
                    if temp:
                        result.extend(temp)
                        temp = []
                    result.append([arr[i - 1][0], rank])
                    rank += 1
            else:
                if temp:
                    result.extend(temp)
                    temp = []
                result.append([arr[i - 1][0], rank])
                rank += 1
        else:
            if temp:
                result.extend(temp)
                temp = []
            result.append([arr[i - 1][0], rank])
            rank += 1
    # 마지막 케이스
    else:
        # 금메달 개수가 같은가
        if arr[i][1] == arr[i - 1][1]:
            # 은메달 개수가 같은가
            if arr[i][2] == arr[i - 1][2]:
                # 동메달 개수가 같은가
                if arr[i][3] == arr[i - 1][3]:
                    # 만약 다 같으면
                    temp.append([arr[i - 1][0], rank])
                    result.extend(temp)
                else:
                    if temp:
                        result.extend(temp)
                        temp = []
                    result.append([arr[i - 1][0], rank])
                    rank += 1
                    result.append([arr[i][0], rank])
            else:
                if temp:
                    result.extend(temp)
                    temp = []
                result.append([arr[i - 1][0], rank])
                rank += 1
                result.append([arr[i][0], rank])
        else:
            if temp:
                result.extend(temp)
                temp = []
            result.append([arr[i - 1][0], rank])
            rank += 1
            result.append([arr[i][0], rank])

for r in range(N):
    if result[r][0] == K:
        print(result[r][1])
        break

