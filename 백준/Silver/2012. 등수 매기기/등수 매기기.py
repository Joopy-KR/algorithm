import sys
input = sys.stdin.readline

N = int(input().rstrip())
result = 0
arr = []
for _ in range(N):
    arr.append(int(input().rstrip()))

arr.sort()
for i in range(N):
    if (i + 1) != arr[i]:
        result += abs(arr[i] - (i + 1))

print(result)