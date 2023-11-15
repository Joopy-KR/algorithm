import sys
input = sys.stdin.readline


N = int(input().rstrip())

arr1 = list(map(int, input().rstrip()))
arr2 = list(map(int, input().rstrip()))

# 그럴 필요 없이 그냥 처음부터 쭉 돌면서 이전꺼만 쭉쭉 보고 가자
# 두가지 경우만 생각하자. 맨 처음껄 누르지 않은 경우와 누른 경우

# 맨 처음껄 누르지 않은 경우
arr1_copy = arr1[:]
not_push_result = 0

for i in range(1, N):
    # 이전꺼만 보면서 가자
    # 이전께 다르다면
    if arr1_copy[i - 1] != arr2[i - 1]:
        # 현재꺼를 눌러야함
        not_push_result += 1
        # 이전꺼 바꾸기
        arr1_copy[i - 1] = arr2[i - 1]
        # 현재꺼 바꾸기
        if arr1_copy[i] == 0:
            arr1_copy[i] = 1
        else:
            arr1_copy[i] = 0
        # 범위 안이라면, 다음것도 눌러줘야함
        if i + 1 < N:
            if arr1_copy[i + 1] == 0:
                arr1_copy[i + 1] = 1
            else:
                arr1_copy[i + 1] = 0

# 다 끝나고 마지막꺼만 비교해주기
if arr1_copy[-1] != arr2[-1]:
    # 불가능함 999999 로 바꿔버리기
    not_push_result = 999999



# 맨 처음껄 누른 경우
arr1_copy = arr1[:]

# 처음꺼 바꾸기
if arr1_copy[0] == 0:
    arr1_copy[0] = 1
else:
    arr1_copy[0] = 0

# 두번째꺼 바꾸기
if arr1_copy[1] == 0:
    arr1_copy[1] = 1
else:
    arr1_copy[1] = 0

push_result = 1

for i in range(1, N):
    # 이전꺼만 보면서 가자
    # 이전께 다르다면
    if arr1_copy[i - 1] != arr2[i - 1]:
        # 현재꺼를 눌러야함
        push_result += 1
        # 이전꺼 바꾸기
        arr1_copy[i - 1] = arr2[i - 1]
        # 현재꺼 바꾸기
        if arr1_copy[i] == 0:
            arr1_copy[i] = 1
        else:
            arr1_copy[i] = 0
        # 범위 안이라면, 다음것도 눌러줘야함
        if i + 1 < N:
            if arr1_copy[i + 1] == 0:
                arr1_copy[i + 1] = 1
            else:
                arr1_copy[i + 1] = 0

# 끝나고 비교하기
if arr1_copy[-1] != arr2[-1]:
    # 불가능함 999999 로 바꿔버리기
    push_result = 999999


# 만약 둘다 불가능이라면
if not_push_result == 999999 and push_result == 999999:
    print(-1)
elif not_push_result != 999999 and push_result != 999999:
    print(min(not_push_result, push_result))
else:
    if not_push_result != 999999:
        print(not_push_result)
    else:
        print(push_result)
