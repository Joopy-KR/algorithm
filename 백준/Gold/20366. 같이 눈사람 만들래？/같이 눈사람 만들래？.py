import sys
input = sys.stdin.readline

N = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
arr.sort()
min_result = float('INF')


def solution():
    global min_result
    for left in range(N - 3):  # a1
        for right in range(3, N):  # a2
            target_sum = arr[left] + arr[right]

            inner_left = left + 1
            inner_right = right - 1
            while inner_left < inner_right:
                temp_sum = arr[inner_left] + arr[inner_right]
                min_result = min(min_result, abs(target_sum - temp_sum))
                if target_sum > temp_sum:
                    inner_left += 1
                elif target_sum < temp_sum:
                    inner_right -= 1
                else:
                    return


solution()
print(min_result)
