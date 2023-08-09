def bubble_sort(lst):
    for i in range(len(lst)-1, 0, -1):
        for j in range(0, i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    new_arr = bubble_sort(arr)
    print(f'#{tc}', *new_arr)
