import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

cant_hear = set()
for _ in range(N):
    cant_hear.add(input().rstrip())

cant_see = set()
for _ in range(M):
    cant_see.add(input().rstrip())


result = sorted(list(cant_see & cant_hear))

print(len(result))
for r in result:
    print(r)