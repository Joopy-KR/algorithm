"""
* 오늘도 다시 복습하는 세그먼트 트리 만드는 법*
1. 트리 초기화
2. 리프 노드 채움
3. 부모 노드 채움
4. 찾음
"""
import math
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

len_k = 0
while True:
    if 2 ** len_k > N:
        break
    len_k += 1

# 1. 트리 초기화
tree = [1] * ((2 ** len_k) * 2)

# 2. 리프 노드 채움
idx = 2 ** len_k
for _ in range(N):
    tree[idx] = int(input()) % 1000000007
    idx += 1

# 3. 부모 노드 채움
for i in range(len(tree) - 1, 1, -1):
    tree[i // 2] *= tree[i] % 1000000007

# 4. 찾음
for _ in range(M + K):
    a, b, c = map(int, input().split())

    b = b + (2 ** len_k) - 1

    # a가 1이면 b번째 수를 c로 바꿈
    if a == 1:
        tree[b] = c % 1000000007

        b_idx = b

        while b_idx > 0:
            b_idx //= 2
            tree[b_idx] = (tree[b_idx * 2] * tree[b_idx * 2 + 1]) % 1000000007


    # a가 2면 b부터 c까지의 곱 출력
    else:
        check = []
        c = c + (2 ** len_k) - 1

        start_idx = b
        end_idx = c

        while start_idx <= end_idx:
            if start_idx % 2 == 1:
                check.append(tree[start_idx] % 1000000007)
            if end_idx % 2 == 0:
                check.append(tree[end_idx] % 1000000007)
            start_idx = (start_idx + 1) // 2
            end_idx = (end_idx - 1) // 2

        print(math.prod(check) % 1000000007)