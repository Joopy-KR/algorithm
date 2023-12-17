import sys
input = sys.stdin.readline

N = int(input().rstrip())

arr = []
for _ in range(N):
    word = input().rstrip()
    arr.append([len(word), word])

arr.sort(key=lambda x: (x[0], x[1]))

duplicate = []

for i in range(len(arr)):
    if arr[i][1] in duplicate:
        pass
    else:
        print(arr[i][1])
        duplicate.append(arr[i][1])