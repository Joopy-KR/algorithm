import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

k = 0
while True:
    k += 1
    if 2 ** k > N:
        break

min_tree = [0] * ((2 ** k) * 2)
max_tree = [0] * ((2 ** k) * 2)

idx = 2 ** k

# 최소, 최대 트리 리프에 값 집어넣기
for _ in range(N):
    n = int(input().rstrip())
    min_tree[idx] = n
    max_tree[idx] = n
    idx += 1

# 리프를 바탕으로 부모 노드 채워나가기
for i in range(len(min_tree) - 1, 1, -1):
    # 최소 트리의 부모가 비어있다면 채워주고
    if min_tree[i // 2] == 0:
        min_tree[i // 2] = min_tree[i]
    # 아니라면 최소 비교하기
    else:
        min_tree[i // 2] = min(min_tree[i // 2], min_tree[i])

    # 최대 역시 마찬가지
    if max_tree[i // 2] == 0:
        max_tree[i // 2] = max_tree[i]
    # 아니라면 최대 비교하기
    else:
        max_tree[i // 2] = max(max_tree[i // 2], max_tree[i])

# 이를 바탕으로 최솟값, 최댓값 출력하기
for _ in range(M):
    min_check = []
    max_check = []
    start_idx, end_idx = map(int, input().rstrip().split())

    # tree 구조에 맞게 인덱스 변화시켜주기
    start_idx = start_idx + (2 ** k) - 1
    end_idx = end_idx + (2 ** k) - 1

    while start_idx <= end_idx:
        if start_idx % 2 == 1:
            # 만약 홀수번째 인덱스라면, 포함시켜주기
            min_check.append(min_tree[start_idx])
            max_check.append(max_tree[start_idx])
        if end_idx % 2 == 0:
            # 만약 짝수번째 인덱스라면, 포함시켜주기
            min_check.append(min_tree[end_idx])
            max_check.append(max_tree[end_idx])

        # depth 변겅하기
        start_idx = (start_idx + 1) // 2
        end_idx = (end_idx - 1) // 2

    # 다 끝났으면 출력해주기
    min_result = min(min_check)
    max_result = max(max_check)

    print(min_result, max_result)