"""
이분탐색 문제란다... 이분탐색으로 풀어보자
정해진 구간이 있으므로, max 값으로부터 반씩 쪼개면서 보자. 결국 mid가 답이 될거다.
이때, mid 만큼 차이를 둔다고 생각했을때, 구간이 몇개 나오는 지 확인해보자.
만약 mid 보다 최대-최소가 크다면 구간 한개가 생긴거다 체크해두고
이렇게 구한 구간이 M(정해진 구간) 보다 작거나 같다면? - 최소값의 가능성이 있으므로 체크하고 end를 mid - 1로 내리기
근데 만약 이렇게 구한 구간의 수가 정해진 구간 수보다 크다면? - 너무 잘게 쪼갠것으로 눈 씻고 찾아봐도 최소의 가능성이 없음 start를 mid + 1로 올리기
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))

# 이때, mid 만큼 차이를 둔다고 생각했을때, 구간이 몇개 나오는 지 확인해보자.
def solve(mid):
    min_val = 10000
    max_val = 0
    section = 1

    # 현재까지의
    for i in range(N):
        if arr[i] < min_val:
            min_val = arr[i]

        if arr[i] > max_val:
            max_val = arr[i]

        # 만약 mid 보다 최대-최소가 크다면 구간 한개가 생긴거다 체크해두고
        if max_val - min_val > mid:
            section += 1
            # 구간이 하나 만들어졌으므로 최대랑 최소 올려주기
            min_val = arr[i]
            max_val = arr[i]

    return section


start = 0
end = max(arr)
result = 10000

while start <= end:
    # 정해진 구간이 있으므로, max 값으로부터 반씩 쪼개면서 보자. 결국 mid가 답이 될거다.
    mid = (start + end) // 2

    # 이렇게 구한 구간이 M(정해진 구간) 보다 작거나 같다면? - 최소값의 가능성이 있으므로 체크하고 end를 mid - 1로 내리기
    if solve(mid) <= M:
        result = min(result, mid)
        end = mid - 1
    # 근데 만약 이렇게 구한 구간의 수가 정해진 구간 수보다 크다면? - 너무 잘게 쪼갠것으로 눈 씻고 찾아봐도 최소의 가능성이 없음 start를 mid + 1로 올리기
    else:
        start = mid + 1


print(result)