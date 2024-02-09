import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

dont = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    dont[a].append(b)
    dont[b].append(a)

result = 0
for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        for k in range(j + 1, N + 1):
            if (j in dont[i]) or (k in dont[i]) or (i in dont[j]) or (k in dont[j]) or (i in dont[k]) or (j in dont[k]):
                continue
            else:
                result += 1

print(result)