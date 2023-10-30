import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

dp = [0] * N

if N == 1:
    print(0)
elif N == 2:
    print(abs(arr[1] - arr[0]))
else:
    dp[0] = 0
    dp[1] = abs(arr[1] - arr[0])

    # 돌면서 최대값 저장해주기
    # 그냥 처음부터 끝까지 노가다로 보자
    for i in range(2, N):
        max_dp = 0
        temp_max = 0
        temp_min = 10001
        # 처음부터 볼 구간까지 돌면서
        for j in range(i, -1, -1):
            temp_result = 0
            temp_max = max(temp_max, arr[j])
            temp_min = min(temp_min, arr[j])
            # 최대값 계산할 시간 (j가 0보다 크다면, 뒤에 dp의 최댓값이 남고 그 전까지 최대-최소로 그룹화 하면 됨)
            if j > 0:
                temp_result += temp_max - temp_min
                temp_result += dp[j-1]
                max_dp = max(temp_result, max_dp)
            else:
                temp_result += temp_max - temp_min
                max_dp = max(temp_result, max_dp)
        # 다 돌면 저장해주기
        dp[i] = max_dp
    print(dp[N - 1])