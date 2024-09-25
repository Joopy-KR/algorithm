"""
1. 간단한 이분탐색 문제
2. 최소거리의 최대값으로 나누면서
3. 정해진 구간을 만족하는지 확인한 후
4. 최소를 갱신하자
"""
import sys
input = sys.stdin.readline

d, n, m = map(int, input().rstrip().split())
arr = [0] + [int(input().rstrip()) for _ in range(n)] + [d]
arr.sort()

# 돌섬을 점프한 거리의 최소가 최대 - 즉 최대한 돌들이 멀리멀리 있어야 함
# 그리고 돌섬은 총 n-m개가 있다. 모두 밟아야 한다.


# 정해놓고 그거보다 작은거의 개수를 세자!!!

def solve(mid):
    cnt = 0
    start = 0
    end = 1
    # 제거 기준으로 세자 - 정해진 최소보다 작으면 보지 말자
    while True:
        if end < len(arr):
            if arr[end] - arr[start] < mid:
                cnt += 1
                end += 1
            else:
                start = end
                end += 1

            # 제거할 수 있는 수보다 많이 빼야하면
            if cnt > m:
                return False
        else:
            break

    if cnt > m:
        return False
    else:
        return True


start = 0
end = d
result = []

if n == m:
    result = [d]
else:
    while start <= end:
        mid = (start + end) // 2

        # 정해진 수보다 작은 애들이 적거나 같게 나왔으면
        # 정답이거나 너무 크게 잡은거다 end를 줄여야함
        if solve(mid):
            start = mid + 1
            result.append(mid)
        # 정해진 수보다 작은 애들이 너무 많이 나왔으면
        else:
            end = mid - 1

print(max(result))