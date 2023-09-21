import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = []
for _ in range(N):
    x, y = map(int, input().rstrip().split())
    arr.append([x, y])

arr.sort()
arr.sort(key=lambda x: (x[0], x[1]))
for i in arr:
    print(*i)