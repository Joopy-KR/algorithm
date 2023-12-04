T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())

    mok = N // H
    nameoji = N % H

    if nameoji == 0:
        print((H * 100) + mok)
    else:
        print((nameoji * 100) + (mok + 1))