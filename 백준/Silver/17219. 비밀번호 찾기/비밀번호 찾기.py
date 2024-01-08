import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

a = {}

for _ in range(N):
    url, password = map(str, input().rstrip().split())

    a[url] = password

for _ in range(M):
    key = input().rstrip()

    print(a[key])