from collections import deque

N, M = map(int, input().split())
Rs = deque()    # 단위 무게당 요금
for _ in range(N):
    Rs.append(int(input()))

Wk = deque()     # 차량의 무게
for _ in range(M):
    Wk.append((int(input())))

park = [0] * N
wait = deque()
cnt = 0
result = 0  # 총 주차 요금
for _ in range(2 * M):
    i = int(input())
    # 차량 i가 주차장에 들어옴
    if i >= 0:
        # 비어있는 공간이 있으면
        if cnt < N:
            cnt += 1
            # 가장 작은 숫자 공간에 주차
            for j in range(len(park)):
                if park[j] == 0:
                    park[j] = i
                    # # 주차 요금에 더해줘야 함
                    result += Rs[j] * Wk[i - 1]
                    break
        # 없으면 대기
        else:
            wait.append(i)

    # 차량 i가 주차장에서 나감
    else:
        cnt -= 1
        for k in range(len(park)):
            if park[k] == -i:
                park[k] = 0
                # 대기중이던 차가 있을 시, 해당 자리에 넣어주어야 함
                if wait:
                    cnt += 1
                    park[k] = wait[0]
                    wait.popleft()
                    result += Rs[k] * Wk[park[k] - 1]
                else:
                    break

print(result)
