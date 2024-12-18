"""
1. 맨 처음 k개만 개수를 검사한다
2. 초밥 번호에 따른 해쉬 테이블을 만들어서 숫자로 관리한다.
3. 왼쪽에 빠져나오는 애 += 1, 오른쪽에 새로 추가되는 애 -= 1
4. 왼쪽 빠져나오는 애가 0이라면 개수 -= 1, 새로 추가되는 애가 1이라면 개수 += 1
5. 다 끝나고 쿠폰 번호가 1이상이라면 pass, 0이라면 += 1을 해준다. <- 반례 발견: max_cnt 찍은 시점에서 이미 쿠폰 포함한 상태였다면? : is_coupon으로 해결

예외: 새로 추가되는 애가 이미 안에 있는 친구라면?
"""
import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().rstrip().split())
sushis = [int(input()) for _ in range(N)]
additional_sushi = sushis[:k]  # 회전초밥이므로 시작과 끝이 이어져야함
sushis.extend(additional_sushi)
sushi_counter = {i: 0 for i in range(1, d + 1)}
max_cnt = 0
max_case = list()
cnt = 0

for i in range(k):
    sushi_counter[sushis[i]] += 1
    if sushi_counter[sushis[i]] == 1:
        cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt

max_case.append(sushis[:k])

left_idx = 0
right_idx = k - 1

while right_idx < len(sushis) - 1:
    # 3. 왼쪽에 빠져나오는 애 -= 1, 오른쪽에 새로 추가되는 애 += 1
    # 4. 왼쪽 빠져나오는 애가 0이라면 개수 -= 1, 새로 추가되는 애가 1이라면 개수 += 1
    sushi_counter[sushis[left_idx]] -= 1
    if sushi_counter[sushis[left_idx]] == 0:
        cnt -= 1
    left_idx += 1

    right_idx += 1
    sushi_counter[sushis[right_idx]] += 1
    if sushi_counter[sushis[right_idx]] == 1:
        cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
            max_case.clear()
            max_case.append(sushis[left_idx: right_idx + 1])
        elif cnt == max_cnt:
            max_case.append(sushis[left_idx: right_idx + 1])

for lst in max_case:
    if c not in lst:
        max_cnt += 1
        break

print(max_cnt)
