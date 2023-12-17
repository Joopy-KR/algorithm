import sys
input = sys.stdin.readline

N = int(input())

k = 0
while True:
    if 2 ** k > N:
        break
    k += 1

tree = [0] * ((2 ** k) * 2)

idx = 2 ** k

arr = list(map(int, input().split()))

for i in arr:
    tree[idx] = i
    idx += 1

for j in range(len(tree) - 1, 1, -1):
    if tree[j // 2] == 0:
        tree[j // 2] = tree[j]
    else:
        tree[j // 2] = min(tree[j // 2], tree[j])


M = int(input())

for _ in range(M):
    a, b, c = map(int, input().split())

    if a == 1:
        b = b + (2 ** k) - 1

        tree[b] = c

        temp_idx = b

        while temp_idx > 0:
            temp_idx //= 2
            tree[temp_idx] = min(tree[temp_idx * 2], tree[temp_idx * 2 + 1])

    else:
        check = []
        start_idx = b + (2 ** k) - 1
        end_idx = c + (2 ** k) - 1

        while start_idx <= end_idx:
            if start_idx % 2 == 1:
                check.append(tree[start_idx])
            if end_idx % 2 == 0:
                check.append(tree[end_idx])

            start_idx = (start_idx + 1) // 2
            end_idx = (end_idx - 1) // 2

        print(min(check))
