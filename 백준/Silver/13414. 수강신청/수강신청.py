import sys

k, l = map(int, sys.stdin.readline().split())

dict = {}
for i in range(l):
    dict[sys.stdin.readline().rstrip()] = i

result = sorted(dict.items(), key = lambda x:x[1])

if (k > len(result)):
    k = len(result)

for i in range(k):
    print(result[i][0])