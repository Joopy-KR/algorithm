"""
거리랑 함께 스택에 푸시하고
돌았는데 더이상 어펜드 할께 없으면 "리프
"""

import sys
input = sys.stdin.readline

N = int(input().rstrip())
ad_lst = [[] * (N+1) for _ in range(N+1)]
for _ in range(N - 1):
    a, b = map(int, input().rstrip().split())
    ad_lst[a].append(b)
    ad_lst[b].append(a)

cnt = 0
result = 0
n = 1
stack = []
stack.append((1, 0))
visited = [0] * (N + 1)
visited[n] = 1

while True:
    is_append = False
    # 스택에서 뽑아서 탐색
    if stack:
        s = stack.pop()
        n = s[0]
        n_cnt = s[1]
        cnt = n_cnt

        visited[n] = 1
        cnt += 1
        for w in range(len(ad_lst[n])):
            if ad_lst[n][w] and visited[ad_lst[n][w]] == 0:
                stack.append((ad_lst[n][w], cnt))
                is_append = True

        # 돌았는데 더이상 어펜드 할께 없으면 "리프"
        if not is_append:
            result += n_cnt
        else:
            continue
    # 스택에 값이 더이상 없으면.
    else:
        break

if result % 2 == 1:
    print('Yes')
else:
    print('No')
