import sys
input = sys.stdin.readline

N, K = map(int, input().split())

arr = list(range(1, N+1))
pointer = 0
result = []

for i in range(N * K):
    pointer += K - 1
    if pointer > len(arr) - 1:
        while pointer > len(arr) - 1:
            pointer -= len(arr)
    result.append(arr.pop(pointer))
    if not arr:
        break

new_result = ', '.join(map(str, result))
print(f'<{new_result}>')
