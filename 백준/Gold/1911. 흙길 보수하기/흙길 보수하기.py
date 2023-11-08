import sys
input = sys.stdin.readline

N, L = map(int, input().rstrip().split())
puddle = []

for _ in range(N):
    puddle.append(tuple(map(int, input().rstrip().split())))

puddle.sort()

# 마지막 널판지 위치
# 만약 널판지가 다음 웅덩이 앞에 온다면
# 웅덩이 끝이랑만 비교할꺼다
last_plank = 0
result = 0

for i in range(N):
    s, e = puddle[i]
    s = max(s, last_plank)
    # 웅덩이 끝이랑 널판지 끝이 딱 맞을때
    if (e - s) % L == 0:
        result += (e - s) // L
        last_plank = e
    # 웅덩이 끝보다 널판지가 남으면은
    else:
        temp = (e - s) // L + 1
        result += temp
        last_plank = s + (temp * L)

print(result)
