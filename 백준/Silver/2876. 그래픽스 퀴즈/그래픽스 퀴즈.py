import sys
input = sys.stdin.readline

N = int(input().rstrip())
grade = [-1] * 6

max_cnt = 0
min_result = 0

for _ in range(N):
    arr = list(map(int, input().split()))
    arr.sort()
    A, B = arr

    # 두 A, B가 다를 경우
    if A != B:
        # 처음이면 일단 넣어주기
        if grade[A] == -1:
            grade[A] = 1
            max_cnt = 1
            min_result = A
        # 처음이 아니라면?
        else:
            grade[A] += 1
            if grade[A] == max_cnt:
                min_result = min(A, min_result)
            elif grade[A] >= max_cnt:
                min_result = A
                max_cnt = grade[A]

        if grade[B] == -1:
            grade[B] = 1
            max_cnt = 1
        # 처음이 아니라면?
        else:
            grade[B] += 1
            if grade[B] == max_cnt:
                min_result = min(B, min_result)
            elif grade[B] >= max_cnt:
                min_result = B
                max_cnt = grade[B]

        # 나오지 않았던 애들은 초기화
        for i in range(1, 6):
            if i not in arr:
                grade[i] = 0

    # 두 A, B가 같을 경우 (한번만 해도 됨ㅎ)
    else:
        # 처음이면 일단 넣어주기
        if grade[A] == -1:
            grade[A] = 1
            max_cnt = 1
            min_result = A
        # 처음이 아니라면?
        else:
            grade[A] += 1
            if grade[A] == max_cnt:
                min_result = min(A, min_result)
            elif grade[A] >= max_cnt:
                min_result = A
                max_cnt = grade[A]

        # 나오지 않았던 애들은 초기화
        for i in range(1, 6):
            if i != A:
                grade[i] = 0

print(max_cnt, min_result)
