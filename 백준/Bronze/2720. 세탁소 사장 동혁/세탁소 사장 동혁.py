Q = 25
D = 10
N = 5
P = 1

T = int(input())
for tc in range(1, T + 1):
    C = int(input())

    Q_cnt = 0
    # 쿼터 빼기
    while True:
        if C - Q >= 0:
            C -= Q
            Q_cnt += 1
        else:
            break

    D_cnt = 0
    # 다임 빼기
    while True:
        if C - D >= 0:
            C -= D
            D_cnt += 1
        else:
            break

    # 니켈 빼기
    N_cnt = 0
    while True:
        if C - N >= 0:
            C -= N
            N_cnt += 1
        else:
            break

    # 페니 빼기
    P_cnt = 0
    while True:
        if C - P >= 0:
            C -= P
            P_cnt += 1
        else:
            break

    print(Q_cnt, D_cnt, N_cnt, P_cnt)