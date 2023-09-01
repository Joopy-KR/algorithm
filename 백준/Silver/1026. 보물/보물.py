import sys
input = sys.stdin.readline

N = int(input().rstrip())
A = list(map(int, input().rstrip().split()))
A.sort()
B = list(map(int, input().rstrip().split()))

# 이미 B에 있는 수를 썼다면, 감옥에 가둬버리기
prison = []
max_val = 0
S = 0

B.sort()
B.reverse()
for i in range(N):
    S += A[i] * B[i]

# for i in range(N):
#     # 아직 쓴 적이 없다면
#     for j in range(N):
#         if B[j] > max_val:
#             if B[j] not in prison:
#                 max_val = B[j]
#     S += A[i] * max_val
#     prison.append(max_val)
#     max_val = 0
# 이 경우 B에 중복이 있을때 처리하지 못함

print(S)
