result = 0

s1 = list(map(int, input().split()))
s2 = list(map(int, input().split()))
s3 = list(map(int, input().split()))
s4 = list(map(int, input().split()))

matrix = [[0] * 100 for _ in range(100)]

for r in range(s1[0], s1[2]):
    for c in range(s1[1], s1[3]):
        matrix[r][c] = 1

for r in range(s2[0], s2[2]):
    for c in range(s2[1], s2[3]):
        matrix[r][c] = 1

for r in range(s3[0], s3[2]):
    for c in range(s3[1], s3[3]):
        matrix[r][c] = 1

for r in range(s4[0], s4[2]):
    for c in range(s4[1], s4[3]):
        matrix[r][c] = 1

for r in range(100):
    for c in range(100):
        if matrix[r][c] == 1:
            result += 1

print(result)