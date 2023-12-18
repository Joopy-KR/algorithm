import sys
input = sys.stdin.readline

N, Q = map(int, input().rstrip().split())

k = 0
while True:
    if 2 ** k > N:
        break
    k += 1

tree = [0] * ((2 ** k) * 2)

arr = list(map(int, input().rstrip().split()))

idx = 2 ** k

for j in arr:
    tree[idx] = j
    idx += 1

for i in range(len(tree) - 1, 1, -1):
    tree[i // 2] += tree[i]

for _ in range(Q):
    x, y, a, b = map(int, input().rstrip().split())

    temtem = [x, y]
    temtem.sort()
    x, y = temtem

    # 답구하기
    start_idx = x + (2 ** k) - 1
    end_idx = y + (2 ** k) - 1

    check = []
    while start_idx <= end_idx:
        if start_idx % 2 == 1:
            check.append(tree[start_idx])
        if end_idx % 2 == 0:
            check.append(tree[end_idx])
        start_idx = (start_idx + 1) // 2
        end_idx = (end_idx - 1) // 2

    print(sum(check))

    # 숫자 바꾸기
    a = a + (2 ** k) - 1

    tree[a] = b

    temp_idx = a
    while temp_idx > 0:
        temp_idx //= 2
        tree[temp_idx] = tree[temp_idx * 2] + tree[temp_idx * 2 + 1]