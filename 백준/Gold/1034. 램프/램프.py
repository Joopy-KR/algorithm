"""
문제를 잘못 판단했다. "행의 최대값"이란 행 전부가 켜져있어야 켜져있는것 하나로 보는것이고
그렇게 전부다 켜진 행이 몇개인지를 구하는 문제였다.

고로 두가지를 우선 판단해야한다.
1. K만큼 다 켰을때 다 켜질 "가능성"이 있는 행인가 (아니라면 행열에 추가하지 않아도 됨)
2. 다 켜질 가능성이란 0의 개수가 K번보다 작거나 같은가, 그리고 작거나 같을때 K가 홀짝에 따라서도 판단해야함.
3. 만약 0의 개수가 K번보다 작거나 같더라도, K-(0의 개수) 가 짝수라면 가능성이 있는것이고, 홀수라면 한개가 남으므로 가능성이 없는 것이다.
4. 그렇게 가능성이 있는 애들로 줄세웠다면, 열별로 탐색하면서 1과 0의 개수를 탐색한다
   - 5. 만약 스위치를 바꾼다면 1은 0으로, 0은 1로 바뀌므로
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
temp_arr = [list(map(int, input().rstrip())) for _ in range(N)]
K = int(input().rstrip())
arr = []


# 1. K만큼 다 켰을때 다 켜질 "가능성"이 있는 행인가 (아니라면 행열에 추가하지 않아도 됨)
for i in range(N):
    temp = temp_arr[i]
    zero_cnt = temp.count(0)
    # 2. 다 켜질 가능성이란 0의 개수가 K번보다 작거나 같은가, 그리고 작거나 같을때 K가 홀짝에 따라서도 판단해야함.
    if zero_cnt <= K:
        # 3. 만약 0의 개수가 K번보다 작거나 같더라도, K-(0의 개수) 가 짝수라면 가능성이 있는것이고, 홀수라면 한개가 남으므로 가능성이 없는 것이다.
        if (K - zero_cnt) % 2 == 0:
            arr.append(temp)

if not arr:
    print(0)
else:
    N = len(arr)
    # 4. 그렇게 가능성이 있는 애들로 줄세웠다면, 운명 공동체를 찾아야한다
    # 운명 공동체란? 0의 위치와 1의 위치가 같은 친구들
    # 운명 공동체끼리는 반드시 1로 만들수 있으므로 결과 개수로 카운트해도 무방함
    # N^2의 노가다로 세자

    # 이미 운명 공동체를 찾았다면 볼 필요 없음
    exclude_lst = []
    you_are_my_destiny = [1] * N
    for a in range(N - 1):
        # 이미 운명공동체가 지어졌다면 패스
        if a in exclude_lst:
            continue
        else:
            # 비교 대상이 될 기준점
            compare = arr[a]
            for j in range(a + 1, N):
                if compare == arr[j]:
                    you_are_my_destiny[a] += 1
                    exclude_lst.append(j)

    print(max(you_are_my_destiny))