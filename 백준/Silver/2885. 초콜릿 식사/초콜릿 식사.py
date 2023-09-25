# 2의 제곱인지 판별기
def is_ee_eu_jegop(n):
    return (n & (n-1)) == 0


K = int(input())
slice = 0
choco = 1
while choco < K:
    choco *= 2

result = choco

while K > 0:
    if K >= choco:
        K -= choco
    else:
        choco //= 2
        slice += 1

print(result, slice)