import sys
input = sys.stdin.readline


def perm(i, k):
    global max_val
    if i == k:
        temp = 0
        for m in range(k - 1):
            temp += abs(p[m] - p[m + 1])
            if temp > max_val:
                max_val = temp
    else:
        for j in range(i, k):
            p[i], p[j] = p[j], p[i]
            perm(i + 1, k)
            p[i], p[j] = p[j], p[i]


max_val = 0
N = int(input().rstrip())
p = list(map(int, input().rstrip().split()))
perm(0, N)
print(max_val)


