N, M = map(int, input().split())

for j in range(1, M + 1):
    print(f'0 {j}')

if (N - 1) != M:
    for i in range(1, N - M):
        print(f'{i} {i + M}')