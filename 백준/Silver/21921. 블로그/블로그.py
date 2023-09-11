import sys
input = sys.stdin.readline

N, X = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))

max_val = 0
now = 0
cnt = 0
end = 0
start = 0
# X개 만큼 처음부터 다 더해주기
for i in range(X):
    end += 1
    now += arr[i]

if now > max_val:
    max_val = now

for j in range(end, N):
    now = now - arr[start] + arr[j]
    if now > max_val:
        cnt = 0
        max_val = now
    elif now == max_val:
        cnt += 1
    start += 1

cnt += 1
if max_val == 0:
    print("SAD")
else:
    print(max_val)
    print(cnt)