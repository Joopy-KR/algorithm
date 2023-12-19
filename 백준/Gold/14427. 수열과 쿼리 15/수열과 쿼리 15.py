"""
세그먼트 트리에 가장 작은 값이랑 인덱스를 같이 넣어주면 된다. 간단간단

와 복사 말고 할당만 하니까 2차원 배열에서 자식 바뀌는 순간 부모가 싹~다 바뀐다 충격
일차원 배열 복사니까 슬라이싱만 해도 되지 않을까?
인덱스 꼬이네... 그냥 카피 하자
"""
import sys
input = sys.stdin.readline

from copy import deepcopy

N = int(input().rstrip())

k = 0
while True:
    if 2 ** k > N:
        break
    k += 1

tree = [0] * ((2 ** k) * 2)

A = list(map(int, input().rstrip().split()))


idx = 2 ** k

for i in range(1, N + 1):
    tree[idx] = [A[i - 1], i]
    idx += 1

# 같으면 인덱스가 작은게 들어감!!!!
for j in range(len(tree) - 1, 1, -1):
    if tree[j // 2] == 0:
        tree[j // 2] = deepcopy(tree[j])
    else:
        # 거꾸로 가는 중이므로 새로 들어가는 애가 무조건 인덱스가 작음!!!
        if tree[j // 2][0] >= tree[j][0]:
            tree[j // 2] = deepcopy(tree[j])

# 0이 아니라면 체크 꼭 해줘야 함! 0들이 중간중간 숨어있어서
# 앞에께([0]) 값, 뒤에께([1]) 인덱스!

M = int(input().rstrip())

for _ in range(M):
    query = list(map(int, input().rstrip().split()))

    if query == [2]:
        # 젤 위에 있는게 최소값 굳이 찾을 필요도 없음
        print(tree[1][1])

    else:
        l, a, b = query

        # a번째 값을 b로 바꾼다
        a = a + (2 ** k) - 1

        tree[a][0] = b

        temp_idx = a

        while temp_idx > 1:
            temp_idx //= 2

            try:
                # 두 자식노드의 값이 같지 않다면
                if tree[temp_idx * 2][0] != tree[temp_idx * 2 + 1][0]:
                    # 단순 값비교만 해주면 됨
                    try:
                        # 양쪽 모두 존재한다면
                        # 인덱스가 작은게 들어감
                        if tree[temp_idx * 2][0] < tree[temp_idx * 2 + 1][0]:
                            tree[temp_idx] = deepcopy(tree[temp_idx * 2])
                        else:
                            tree[temp_idx] = deepcopy(tree[temp_idx * 2 + 1])

                    except:
                        # 양쪽 모두 존재하지 않는다면 (왼쪽만 존재한다면)
                        # 그냥 넣어주면 됨 ㅇㅅㅇ
                        tree[temp_idx] = deepcopy(tree[temp_idx * 2])

                # 두 자식 노드의 값이 같다면?!
                else:
                    # 당연하게도 인덱스가 작은게 들어감
                    tree[temp_idx] = deepcopy(tree[temp_idx * 2])

            # 오른쪽 자식이 0이라면?!
            except TypeError:
                # 부모에 자식 값이 들어가면 됨
                tree[temp_idx] = deepcopy(tree[temp_idx * 2])



