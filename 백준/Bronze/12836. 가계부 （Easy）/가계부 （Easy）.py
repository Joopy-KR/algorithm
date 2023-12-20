import sys
input = sys.stdin.readline

N, Q = map(int, input().rstrip().split())

k = 0
while True:
    if 2 ** k > N:
        break
    k += 1

tree = [0] * ((2 ** k) * 2)

for _ in range(Q):
    a, b, c = map(int, input().rstrip().split())

    if a == 1:
        b = b + (2 ** k) - 1

        tree[b] += c

        temp_idx = b

        while temp_idx > 1:
            temp_idx //= 2
            tree[temp_idx] = tree[temp_idx * 2] + tree[temp_idx * 2 + 1]

    else:
        start_idx = b + (2 ** k) - 1
        end_idx = c + (2 ** k) - 1

        check = []

        while start_idx <= end_idx:
            if start_idx % 2 == 1:
                check.append(tree[start_idx])
            if end_idx % 2 == 0:
                check.append(tree[end_idx])

            start_idx = (start_idx + 1) // 2
            end_idx = (end_idx - 1) // 2

        print(sum(check))