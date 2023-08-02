def bubble_sort(a, N):
    for i in range(N-1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

def counting_sort(ori, temp, k):
    # 1. 카운팅 리스트를 만들어준다. (k+1만큼)
    c = [0] * (k+1)

    # 2. 원래 배열을 돌면서, 각 수를 세준다.
    for i in range(len(ori)):
        c[ori[i]] += 1

    # 3. 카운트 배열을 누적합으로 바꿔준다
    for j in range(1, len(c)):
        c[j] += c[j-1]

    # 4. 원래 배열의 뒤에서부터, 인덱스만큼 count -1 해주고 이를 인덱스로 새로운 배열에 추가해준다.
    for u in range(len(ori)-1, -1, -1):
        c[ori[u]] -= 1
        temp[c[ori[u]]] = ori[u]

    return temp


T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    new_arr = bubble_sort(arr, 10)
    print(new_arr[-3])