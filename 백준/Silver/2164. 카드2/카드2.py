"""
1. 큐 만들어서
2. 제일 위에 있는거 하나 버린후
3. 그 다음 front에 있는걸 맨 뒤로 옮긴다
4. 하나 남을때까지 반복
"""
N = int(input())
cnt = N
q = [0] * 1000000
front = rear = -1

for i in range(N):
    q[i] = i + 1
    rear += 1

while cnt != 1:
    # 2. 제일 위에 있는거 하나 버린후
    front += 1
    cnt -= 1
    # 3. 그 다음 front에 있는걸 맨 뒤로 옮긴다
    front += 1
    rear += 1
    q[rear] = q[front]

print(q[rear])