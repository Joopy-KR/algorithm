import sys
input = sys.stdin.readline

T = int(input().rstrip())

for tc in range(1, T + 1):
    W = input()
    K = int(input().rstrip())

    is_answer = False

    check = {}

    for w in W:
        check[w] = check.get(w, 0) + 1

    min_result = len(W)
    max_result = -1

    idx_dict = {}

    for i in range(len(W)):
        if check[W[i]] < K:
            continue

        is_answer = True

        idx_dict[W[i]] = idx_dict.get(W[i], []) + [i]

    for key, value in idx_dict.items():
        for j in range(len(value) - K + 1):
            max_result = max(max_result, value[j + K - 1] - value[j] + 1)
            min_result = min(min_result, value[j + K - 1] - value[j] + 1)

    if is_answer:
        print(min_result, max_result)
    else:
        print(-1)