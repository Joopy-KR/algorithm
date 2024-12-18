"""
1. 우선 처음 k개의 경우를 생각한 뒤
2. 왼쪽, 오른쪽 인덱스 잡고 하나씩 옮겨가며 오른쪽꺼 판단하기
3. 매 이동시마다, 쿠폰이 포함되었는지 확인하기

예외1. "회전" 초밥이므로 처음 k개 저장해뒀다가 나중에 포함해서 순회돌기
예외2. 최대일 경우 쿠폰번호 포함되었는지 확인하기
"""
import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().rstrip().split())
sushis = [int(input()) for _ in range(N)]
sushis.extend(sushis[:k])
sushi_counter = {i: 0 for i in range(1, d + 1)}
now_cnt = 0
max_cnt = -1
is_coupon = False

# 1. 우선 처음 k개의 경우를 생각한 뒤
for i in range(k):
    sushi = sushis[i]
    if sushi == c:
        is_coupon = True
    sushi_counter[sushi] += 1
    if sushi_counter[sushi] == 1:
        now_cnt += 1
max_cnt = now_cnt

# 2. 왼쪽, 오른쪽 인덱스 잡고 하나씩 옮겨가며 오른쪽꺼 판단하기
left_idx = 0
right_idx = k - 1
while right_idx < len(sushis) - 1:
    sushi_counter[sushis[left_idx]] -= 1
    if sushi_counter[sushis[left_idx]] == 0:
        now_cnt -= 1
    left_idx += 1

    right_idx += 1
    sushi_counter[sushis[right_idx]] += 1
    if sushi_counter[sushis[right_idx]] == 1:  # 새로온 초밥이라면
        now_cnt += 1

    if sushi_counter[c] > 0:  # 안에 쿠폰이 있으면
        max_cnt = max(max_cnt, now_cnt)
    else:
        max_cnt = max(max_cnt, now_cnt + 1)

print(max_cnt)