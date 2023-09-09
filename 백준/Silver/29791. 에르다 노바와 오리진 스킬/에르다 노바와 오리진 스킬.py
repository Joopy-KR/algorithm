N, M = map(int, input().split())

fifth = list(map(int, input().split()))
fifth.sort()
sixth = list(map(int, input().split()))
sixth.sort()

no_move = 0
cool_time_fifth = 0
for i in range(N):
    if fifth[i] >= cool_time_fifth:
        no_move += 1
        cool_time_fifth = fifth[i] + 100

real_no_move = 0
cool_time_sixth = 0
for j in range(M):
    if sixth[j] >= cool_time_sixth:
        real_no_move += 1
        cool_time_sixth = sixth[j] + 360

print(no_move, real_no_move)