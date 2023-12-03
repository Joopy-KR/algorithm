"""
8씩 늘어난다..?!

왼쪽 위
1 5 17 37
 4 12 20

제일 왼쪽 위를 구하는 공식:

오른쪽
1 2 11 28
 1 9  17


1. 제일 왼쪽 위에 숫자를 구한다음에
2. 첫째 "열"의 숫자를 다 구하고
3. 각 열별로 공식에 따라 나머지 숫자를 채운 후
4. 출력한다.

---- 까지가 실패한 풀이. 이 공식이 일정하지 않다...

그냥 그려야겠는데?
"""
import sys
input = sys.stdin.readline

r1, c1, r2, c2 = map(int, input().rstrip().split())

arr = [[0] * (c2 - c1 + 1) for _ in range(r2 - r1 + 1)]

all_cnt = (c2 - c1 + 1) * (r2 - r1 + 1)

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

r = 0
c = 0
now = 1
direction = 1
togo = 1

# 한 방향당 같은 횟수로 두번씩 움직인다?!

while all_cnt > 0:
    for _ in range(2):
        for _ in range(togo):
            if r1 <= r <= r2 and c1 <= c <= c2:
                arr[r - r1][c - c1] = now
                all_cnt -= 1
                max_len = now
            r += dr[direction]
            c += dc[direction]
            now += 1

        # 방향 바꾸기
        direction = (direction - 1) % 4

    # 두번 돌았다면 다음번엔 한번 더가기
    togo += 1

max_len = len(str(max_len))

for r in range(r2 - r1 + 1):
    for c in range(c2 - c1 + 1):
        print(str(arr[r][c]).rjust(max_len), end=" ")
    print()
