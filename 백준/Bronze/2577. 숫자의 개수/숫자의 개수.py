A = int(input())
B = int(input())
C = int(input())

mult = str(A * B * C)
cnt = [0] * 10

for i in range(10):
    for s in mult:
        if s == str(i):
            cnt[i] += 1

for r in cnt:
    print(r)