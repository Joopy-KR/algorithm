max_val = 0
max_idx = 0
for i in range(1, 10):
    temp = int(input())
    if temp > max_val:
        max_val = temp
        max_idx = i

print(max_val)
print(max_idx)