T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))[::-1]
    result = 0
    # 1. 첫번째 값을 max_val 에 담아주고
    max_val = arr[0]

    for i in range(1, N):
        # 2. 그리고 그 다음 수(+1)랑 비교를 했을때
        # 다음수가 max_val보다 크다면, 갱신
        if arr[i] > max_val:
            max_val = arr[i]
            continue
        # 3. 안크다면, 그 차이만큼을 result에 담기
        else:
            result += max_val - arr[i]

    print(f'#{tc} {result}')