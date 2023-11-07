first = [""] + list(map(str, input()))
second = [""] + list(map(str, input()))
arr = [[""] * len(second) for _ in range(len(first))]

for r in range(1, len(first)):
    for c in range(1, len(second)):
        if first[r] == second[c]:
            arr[r][c] = arr[r - 1][c - 1] + first[r]
        else:
            if len(arr[r - 1][c]) > len(arr[r][c - 1]):
                arr[r][c] = arr[r - 1][c]
            else:
                arr[r][c] = arr[r][c - 1]

result = arr[-1][-1]

if len(result) > 0:
    print(len(result))
    print(result)
else:
    print(0)


