def solve(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        f = [0] * (n + 1)
        f[0] = 1
        f[1] = 1
        f[2] = 2
        for i in range(3, n + 1):
            f[i] = f[i - 1] + f[i - 2]
        return f[n]



from collections import deque

N = int(input())
M = int(input())
fixed = deque()
for _ in range(M):
    fixed.append(int(input()))

# 고정석이 있을 때
if M:
    result = 1
    start = 1
    while fixed:
        end = fixed.popleft()
        result *= solve(end - start)
        start = end + 1
    if start != N:
        end = N + 1
        result *= solve(end - start)
# 고정석이 없을 때
else:
    result = solve(N)

print(result)
