"""
S: 부패 속도 (arr[0])
L: 유통기한  (arr[1])
O: 중요한 재료인가 (arr[2])

생각을 바꿔보자... 빼는 개수를 세는게 아니라 애초에 k 개만큼 큰 애들을 빼놓고 시작하는거다...
"""
import sys
input = sys.stdin.readline

N, G, K = map(int, input().rstrip().split())
arr = []
# S, L, O
for _ in range(N):
    arr.append(list(map(int, input().rstrip().split())))


def germ(x, lst):
    return lst[0] * max(1, x - lst[1])


def solve(mid):

    # 세균 수
    germ_cnt = 0
    # 뺄 수 있는 세균 수 담아둘 리스트
    stack = []

    # 배열을 돌면서
    for lst in arr:
        # 뺄 수 있다면
        if lst[2] == 1:
            # 세균 계산하고
            temp = germ(mid, lst)
            # 총 세균 수에 세균 더해주고
            germ_cnt += temp
            # 스택에 담아준다
            stack.append(temp)
        # 뺄 수 없다면
        else:
            # 총 세균 수에 더해주기만 한다
            germ_cnt += germ(mid, lst)

    # 이후 스택을 정렬하고 (제일 큰 세균 수가 뒤로 감)
    stack.sort()

    # K번 만큼
    for _ in range(K):
        # 스택이 남아있다면
        if stack:
            # 뽑아서 빼준다
            germ_cnt -= stack.pop()

    # 이후 남아있는 최소 세균 수를 리턴
    return germ_cnt


start = 0
end = int(2e9)
result = 0

while start <= end:
    mid = (start + end) // 2

    # 정해진 범위 내에 먹을 수 있다면
    if solve(mid) <= G:
        result = max(result, mid)
        start = mid + 1
    else:
        end = mid - 1


print(result)
