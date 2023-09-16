"""
1. 간단하네
2. 오른쪽에 더 싼집이 있으면
3. 거기까지만 어떻게든 이동하자ㅇㅇ
4. 단계적으로
"""

import sys
# input = sys.stdin.readline

N = int(input())
city = list(map(int, input().split()))
price = list(map(int, input().split()))

result = 0
start = 0
while start < N - 1:
    length = 0
    for j in range(start + 1, N):
        # 2. 오른쪽에 더 싼집이 있으면
        if price[j] < price[start]:
            length += city[j - 1]
            result += price[start] * length
            start = j
            break
        else:
            length += city[j - 1]
    else:
        result += price[start] * length
        break

print(result)