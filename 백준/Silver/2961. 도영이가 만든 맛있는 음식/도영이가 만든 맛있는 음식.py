import sys
input = sys.stdin.readline

N = int(input().rstrip())
sours = []
bitters = []
min_result = sys.maxsize

for _ in range(N):
    s, b = map(int, input().rstrip().split())
    sours.append(s)
    bitters.append(b)

for i in range(2 ** N):
    temp_sour = 1
    temp_bitter = 0
    is_avail = False
    for j in range(len(sours)):  # 재료 개수
        if i & (1 << j):
            temp_sour *= sours[j]
            temp_bitter += bitters[j]
            is_avail = True
    if is_avail:
        min_result = min(min_result, abs(temp_sour - temp_bitter))

print(min_result)