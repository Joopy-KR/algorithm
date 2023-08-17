def cycle(q):
    global front
    global rear
    global result
    cnt = 0
    while q[rear] != 0:
        if cnt == 5:
            cnt = 0
        cnt += 1
        front += 1
        q[front] -= cnt
        if q[front] < 0:
            q[front] = 0
        rear += 1
        q[rear] = q[front]
    for o in q[front+1:rear+1]:
        if o == None:
            pass
        else:
            result += str(o)
            result += ' '
    return result


for tc in range(1, 11):
    T = int(input())
    Q = [None] * 1000000
    front = -1
    rear = -1
    arr = list(map(int, input().split()))
    result = ''

    for i in range(8):
        Q[i] = arr[i]
        rear += 1

    print(f'#{tc} {cycle(Q)}')