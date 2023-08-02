def bubble_sort(a, N):
    for i in range(N-1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a


T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    new_arr = bubble_sort(arr, 10)
    print(new_arr[-3])