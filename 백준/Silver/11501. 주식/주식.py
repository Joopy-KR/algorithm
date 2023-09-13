"""
1. 자기한테 사서 오른쪽에 있는 최대값이랑 계산해준다
2. 계속 돌 필요는 없다... 최대값에서 다시 시작하면 되므로
"""
import sys
input = sys.stdin.readline

T = int(input())
for tc in range(1, T + 1):
    N = int(input().rstrip())
    stock = list(map(int, input().rstrip().split()))

    # 거꾸로 돌자
    # 커지면 좋고 커지다가 말면 빼주고결론

    # 처음부터 끝나기 직전까지
    temp = []
    max_val = stock[-1]
    min_val = 100000
    result = 0
    for i in range(N-1, 0, -1):
        if stock[i - 1] <= max_val:
            result += max_val - stock[i - 1]
        else:
            max_val = stock[i - 1]

    print(result)

