"""
6 -> 2 4 4 2
8 -> 2 6 6 2 4 4

이런식으로 짝수들로 쪼개서 곱한거 더하는게 그거같다.
일단 엣지케이스 없다고 생각하고 풀어보자.
"""

def solution(n):
    if n % 2 == 1:
        return 0
    else:
        dp = [0] * (n + 5)
        dp[2] = 3
        dp[4] = 11

        for i in range(6, n + 1, 2):
            temp_sum = dp[i - 2] * 3
            # i를 짝수의 조합으로 쪼개야함
            for j in range(2, i - 3, 2):
                temp_sum += dp[j] * 2
            temp_sum += 2
            dp[i] = temp_sum % 1000000007
            
        return dp[n]