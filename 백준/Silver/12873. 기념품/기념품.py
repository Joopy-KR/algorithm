N = int(input())
arr = [i for i in range(1, N + 1)]
t = 0
cnt = N
boj = 0
while cnt != 1:
    t += 1
    move = ((t ** 3) % len(arr)) - 1
    if boj + move >= len(arr):
        while boj + move >= len(arr):
            boj -= len(arr)
    elif boj + move < 0:
        while boj + move < 0:
            boj += len(arr)
    boj += move
    arr.pop(boj)
    cnt -= 1

print(*arr)