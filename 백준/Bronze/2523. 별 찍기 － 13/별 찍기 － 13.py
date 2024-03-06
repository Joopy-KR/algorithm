import sys
input = sys.stdin.readline

N = int(input().rstrip())
for i in range(1, N):
    print('*' * i)
print('*' * N)
for j in range(N - 1, 0, -1):
    print('*' * j)