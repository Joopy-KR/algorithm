import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = [list(map(str, input().rstrip().split())) for _ in range(N)]

for i in range(len(arr)):
    arr[i][0] = int(arr[i][0])

arr.sort(key=lambda x:x[0])

for i in arr:
    print(i[0], i[1])