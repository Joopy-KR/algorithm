T = int(input())

A = 300
B = 60
C = 10

A_cnt = 0
while True:
    if T - A >= 0:
        T -= A
        A_cnt += 1
    else:
        break

B_cnt = 0
while True:
    if T - B >= 0:
        T -= B
        B_cnt += 1
    else:
        break

C_cnt = 0
while True:
    if T - C >= 0:
        T -= C
        C_cnt += 1
    else:
        break

if T == 0:
    print(A_cnt, B_cnt, C_cnt)
else:
    print(-1)