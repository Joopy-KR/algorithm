# dp[i] = dp[i - 1] + dp[i - 2]
import sys
input = sys.stdin.readline

T = int(input().rstrip())
for tc in range(1, T + 1):
    N = int(input().rstrip())
    if N == 0:
        print(1, 0)
        continue
    elif N == 1:
        print(0, 1)
        continue
    dp_zero = [0] * (N + 1)
    dp_zero[0] = 1
    dp_zero[1] = 0

    dp_one = [0] * (N + 1)
    dp_one[1] = 1

    for i in range(2, N + 1):
        dp_zero[i] = dp_zero[i - 1] + dp_zero[i - 2]
        dp_one[i] = dp_one[i - 1] + dp_one[i - 2]

    print(dp_zero[N], dp_one[N])
