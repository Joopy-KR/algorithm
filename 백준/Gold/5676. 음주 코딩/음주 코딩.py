import math
import sys
input = sys.stdin.readline

while True:
    try:
        N, K = map(int, input().rstrip().split())

        X = list(map(int, input().rstrip().split()))

        for j in range(len(X)):
            if X[j] > 0:
                X[j] = 1
            elif X[j] < 0:
                X[j] = -1

        len_k = 0
        while True:
            if 2 ** len_k > N:
                break
            len_k += 1

        tree = [1] * ((2 ** len_k) * 2)

        idx = 2 ** len_k

        for x in X:
            tree[idx] = x
            idx += 1

        for i in range(len(tree) - 1, 1, -1):
            tree[i // 2] *= tree[i]


        result = []

        for _ in range(K):
            a, b, c = map(str, input().rstrip().split())

            b = int(b)
            c = int(c)
            if a == 'C':
                b = b + (2 ** len_k) - 1
                if c > 0:
                    c = 1
                elif c < 0:
                    c = -1

                tree[b] = c

                b_idx = b
                while b_idx > 0:
                    b_idx //= 2
                    tree[b_idx] = tree[b_idx * 2] * tree[b_idx * 2 + 1]

            else:
                check = []
                start_idx = b + (2 ** len_k) - 1
                end_idx = c + (2 ** len_k) - 1

                while start_idx <= end_idx:
                    if start_idx % 2 == 1:
                        check.append(tree[start_idx])
                    if end_idx % 2 == 0:
                        check.append(tree[end_idx])
                    start_idx = (start_idx + 1) // 2
                    end_idx = (end_idx - 1) // 2

                temp_result = math.prod(check)

                if temp_result > 0:
                    result.append('+')
                elif temp_result == 0:
                    result.append('0')
                elif temp_result < 0:
                    result.append('-')

        print(''.join(result))

    except:
        break