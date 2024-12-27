import sys

def solution(numbers, target):
    N = len(numbers)
    answer = 0
    max_num = 2 ** N
    for i in range(max_num):
        temp_sum = 0
        for k in range(N):
            if i & (1 << k):
                temp_sum += numbers[k]
            else:
                temp_sum -= numbers[k]
        
        if temp_sum == target:
            answer += 1
    
    return answer