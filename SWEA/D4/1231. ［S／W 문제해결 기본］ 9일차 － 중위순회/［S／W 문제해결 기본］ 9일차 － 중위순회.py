def inorder(n, tree):
    global tc
    global result
    if n:
        inorder(ch1[n], tree)
        result += tree[n - 1][1]
        inorder(ch2[n], tree)
    return result

for tc in range(1, 11):
    N = int(input())

    ch1 = [0] * (N + 1)
    ch2 = [0] * (N + 1)
    tree = []
    result = ''

    for _ in range(N):
        arr = list(map(str, input().split()))
        tree.append([arr[0], arr[1]])

        if arr[2:]:
            for i in arr[2:]:
                if ch1[int(arr[0])] == 0:  # 자식 1이 아직 없으면
                    ch1[int(arr[0])] = int(i)
                else:
                    ch2[int(arr[0])] = int(i)

    print(f'#{tc} {inorder(1, tree)}')