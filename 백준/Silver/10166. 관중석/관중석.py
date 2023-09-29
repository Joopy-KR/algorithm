import math
import sys

input = sys.stdin.readline

a, b = map(int, input().split())
check = [[0] * b for _ in range(b)]  # 기약분수를 저장하기 위한 2차원 배열
cnt = 0  # 좌석 수

for i in range(a, b + 1):
    for j in range(1, i):
        # 최대공약수
        g = math.gcd(i, j)
        # j / i 를 기약분수로 나타내기 위해 최대공약수로 나눈다
        x, y = j // g, i // g
        # 처음 나온 기약분수라면 저장 및 카운트
        if not check[x - 1][y - 1]:
            check[x - 1][y - 1] = 1
            cnt += 1

print(cnt + 1)