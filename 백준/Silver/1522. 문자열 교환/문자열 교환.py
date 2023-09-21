"""
a가 8번 연속되어 있어야 하는 것이므로
8개씩 묶으면서 안의 b와 밖의 a를 바꿨을 때
그 개수가 최소가 되면 됨.
즉, a의 개수만큼 묶으면서 끝까지 이동해야 한다.
"""
import sys
input = sys.stdin.readline

arr = list(map(str, input().rstrip()))
a = 0
b = 0
# a, b 개수 세기
for s in arr:
    if s == 'a':
        a += 1
    else:
        b += 1

min_b = 10000
# 넘어가면 처음부터 봐야하므로 거꾸로 봐야함
# 즉, a의 개수만큼 묶으면서 끝까지 이동해야 한다.
for window in range(len(arr)-1, -1, -1):
    temp = 0
    # 시작: window, 끝: window - a + 1
    for w in range(window, window - a, -1):
        # 안에 있는 b랑 밖에 있는 a를 바꿔야 하므로
        # 안에 있는 b 개수를 세주면 그만 아닌가?
        if arr[w] == 'b':
            temp += 1
    min_b = min(temp, min_b)

print(min_b)