import sys
input = sys.stdin.readline

money = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

bnp_budget = money
bnp_stock = 0
timing_budget = money
timing_stock = 0

# 첫날 풀매수
bnp_stock += bnp_budget // arr[0]
bnp_budget -= (bnp_budget // arr[0]) * arr[0]

# 둘째날 풀매수
bnp_stock += bnp_budget // arr[1]
bnp_budget -= (bnp_budget // arr[1]) * arr[1]

# 셋째날 풀매수
bnp_stock += bnp_budget // arr[2]
bnp_budget -= (bnp_budget // arr[2]) * arr[2]

for i in range(3, len(arr)):
    # 준현이 bnp 매매하기
    bnp_stock += bnp_budget // arr[i]
    bnp_budget -= (bnp_budget // arr[i]) * arr[i]

    # 성민이 timing 매매하기
    if arr[i - 3] < arr[i - 2] < arr[i - 1] < arr[i]:
        # 풀매도
        timing_budget += timing_stock * arr[i]
        timing_stock = 0
    elif arr[i - 3] > arr[i - 2] > arr[i - 1] > arr[i]:
        # 풀매수
        timing_stock += timing_budget // arr[i]
        timing_budget -= (timing_budget // arr[i]) * arr[i]


bnp_total = bnp_budget + (bnp_stock * arr[13])
timing_total = timing_budget + (timing_stock * arr[13])

if bnp_total > timing_total:
    print('BNP')
elif bnp_total < timing_total:
    print('TIMING')
else:
    print('SAMESAME')