from collections import deque
import sys
input = sys.stdin.readline


def solution(p: list, arr: deque):
    is_reversed = False
    for func in p:
        if func == "R":
            if is_reversed:
                is_reversed = False
            else:
                is_reversed = True
        elif func == "D":
            if len(arr) == 0:
                print("error")
                return
            if not is_reversed:
                arr.popleft()
            else:
                arr.pop()
    else:
        if is_reversed:
            arr.reverse()
            print("[" + ",".join(list(arr)) + "]")
        else:
            print("[" + ",".join(list(arr)) + "]")
        return


T = int(input().rstrip())
for tc in range(1, T + 1):
    p = list(input().rstrip())
    n = int(input().rstrip())
    temp_arr = input().rstrip()
    arr = temp_arr[1:len(temp_arr) - 1].split(",")
    if arr[0] == '':
        arr = []
    queue = deque(arr)
    solution(p, queue)
