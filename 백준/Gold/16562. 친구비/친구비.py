"""
딱봐도 그래프, 딱봐도 다익스트라
모든 정점에 대해 cost 2 내로 연결되어있다면 최소비용 출력
하나라도 안된다면 Oh no

다익스트라가 아니네?
플로이드 와샬하면 시간초과 날텐데?

유니온 파인드로 해결해보자
"""
import sys
INF = sys.maxsize
input = sys.stdin.readline

N, M, K = map(int, input().rstrip().split())

A = [0] + list(map(int, input().rstrip().split()))

parent = [0] * (N + 1)

for i in range(1, N + 1):
    parent[i] = i


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
        return parent[x]
    return x


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for j in range(M):
    v, w = map(int, input().rstrip().split())
    union(v, w)


for l in range(1, N + 1):
    find(l)


# 집합이 총 몇개가 생기는지 확인하고
# 각 집합별로 최소비용 계산해야 함
size = max(parent)

check = [INF] * (size + 1)

for i in range(1, N + 1):
    check[parent[i]] = min(check[parent[i]], A[i])

result = 0


for k in range(1, len(check)):
    if check[k] != INF:
        result += check[k]


if result > K:
    print('Oh no')
else:
    print(result)