"""
1. 각 과목별로 넣어야 하는 최소 마일리지를 구한다음에
2. 모아서 정렬
3. 이후 적게 넣어도 되는거부터 해서 총 몇개 들을수 있는지 구하기
"""
import sys
input = sys.stdin.readline


N, M = map(int, input().rstrip().split())


sugang_mile = []


for _ in range(N):
    P, L = map(int, input().rstrip().split())
    temp = list(map(int, input().rstrip().split()))

    temp.sort(reverse=True)
    if P < L:
        sugang_mile.append(1)
    else:
        sugang_mile.append(temp[L - 1])


sugang_mile.sort()

result = 0
temp_sum = 0

for i in sugang_mile:
    if temp_sum + i <= M:
        result += 1
        temp_sum += i
    else:
        break

print(result)

