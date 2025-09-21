import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = list(map(int, input().split()))
M = max(arr)

temp = 0
for i in arr:
    temp += i / M * 100

print(temp / len(arr))