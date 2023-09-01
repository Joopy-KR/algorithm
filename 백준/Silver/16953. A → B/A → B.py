A, B = map(int, input().split())
cnt = 1
while B != A:
    cnt += 1
    if str(int(B))[-1] == '1':
        B //= 10
    else:
        B /= 2
    if B < A:
        cnt = -1
        break

print(cnt)