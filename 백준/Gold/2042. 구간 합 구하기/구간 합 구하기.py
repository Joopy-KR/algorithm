"""
* 세그먼트 트리를 만드는 법*
1. 트리를 초기화한다 (k 구하는법 = 2 ** k > N 을 구한다) (트리의 개수 = (2 ** k) * 2)
2. 주어진 정보를 바탕으로 리프 노드를 채운다 (idx 변화 시켜줘야함)
3. 리프노드를 기준으로 부모노드를 채운다
4. 이를 바탕으로 구간을 구한다
    4-0. idx 변화 시켜주고
    4-1. start_idx <= end_idx 동안
    4-2. start_idx % 2 == 1 이라면 오른쪽에 있는 것이므로 포함
    4-3. 마찬가지로 end_idx % 2 == 0 이라면 왼쪽에 있는 것이므로 포함
    4-4. (start_idx + 1) // 2 로 이동
    4-5. (end_idx - 1) // 2 로 이동
"""
import sys
input = sys.stdin.readline

N, M, K = map(int, input().rstrip().split())

# 1. 트리를 초기화한다 (k 구하는법 = 2 ** k > N 을 구한다) (트리의 개수 = (2 ** k) * 2)
len_k = 0
while True:
    if 2 ** len_k > N:
        break
    len_k += 1

tree = [0] * ((2 ** len_k) * 2)

# 2. 주어진 정보를 바탕으로 리프 노드를 채운다 (idx 변화 시켜줘야함)
idx = 2 ** len_k

for _ in range(N):
    tree[idx] = int(input().rstrip())
    idx += 1

# 3. 리프노드를 기준으로 부모노드를 채운다
for child_node in range(len(tree) - 1, 1, -1):
    parent_node = child_node // 2
    tree[parent_node] += tree[child_node]

# 4. 이를 바탕으로 구간을 구한다 (단, 변경과 함께 구할 것)
for _ in range(M + K):
    a, b, c = map(int, input().rstrip().split())

    # a가 1이면 b번째 수를 c로 바꿈
    if a == 1:
        # 해당 리프 노드를 바꾼 후
        b = b + (2 ** len_k) - 1

        # 여기 있는 sub 만큼 "더해" 줘야함
        sub = c - tree[b]
        tree[b] = c

        # 최상위 부모 노드까지만 타고타고 가서 바꾸면 된다 (바꾼 수의 차 만큼)
        temp_idx = b

        while temp_idx > 0:
            temp_idx = temp_idx // 2
            tree[temp_idx] += sub

    # a가 2이면 b번째 수부터 c번째 수까지의 합을 구하여 출력
    elif a == 2:
        # 4-0. idx 변화 시켜주고
        b = b + (2 ** len_k) - 1
        c = c + (2 ** len_k) - 1

        temp = [b, c]
        temp.sort()
        start_idx, end_idx = temp

        check = []

        # 4-1. start_idx <= end_idx 동안
        while start_idx <= end_idx:
            # 4-2. start_idx % 2 == 1 이라면 오른쪽에 있는 것이므로 포함
            if start_idx % 2 == 1:
                check.append(tree[start_idx])
            # 4-3. 마찬가지로 end_idx % 2 == 0 이라면 왼쪽에 있는 것이므로 포함
            if end_idx % 2 == 0:
                check.append(tree[end_idx])
            # 4-4. (start_idx + 1) // 2 로 이동
            start_idx = (start_idx + 1) // 2
            # 4-5. (end_idx - 1) // 2 로 이동
            end_idx = (end_idx - 1) // 2

        print(sum(check))
