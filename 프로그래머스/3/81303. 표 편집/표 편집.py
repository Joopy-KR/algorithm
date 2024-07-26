def solution(n, k, cmd):
    now = k
    answer = ['O'] * n  
    arr = { i:[i - 1, i + 1] for i in range(n) }
    arr[0] = [None, 1]
    arr[n - 1] = [n - 2, None]
    deleted_stack = []
    
    for c in cmd:
        # 현재 선택된 행에서 X칸 위에 있는 행을 선택
        if c[0] == "U":
            for _ in range(int(c[2:])):
                now = arr[now][0]

        # 현재 선택된 행에서 X칸 아래에 있는 행을 선택
        elif c[0] == "D":
            for _ in range(int(c[2:])):
                now = arr[now][1]

        # 현재 선택된 행을 삭제한 후, 바로 아래 행을 선택
        elif c[0] == "C":
            answer[now] = 'X'
            prev, next = arr[now]
            deleted_stack.append([now, prev, next])
            # 삭제된 행이 가장 마지막 행인 경우 바로 윗 행을 선택
            if next == None:
                arr[prev][1] = None
                now = prev
            elif prev == None:
                arr[next][0] = None
                now = next
            else:
                arr[prev][1] = next
                arr[next][0] = prev
                now = next
                
        # 가장 최근에 삭제된 행을 원래대로 복구
        elif c[0] == "Z":
            new_now, new_prev, new_next = deleted_stack.pop()
            answer[new_now] = 'O'
            if new_prev is None:
                arr[new_next][0] = new_now
            else:
                arr[new_prev][1] = new_now
            if new_next is None:
                arr[new_prev][1] = new_now
            else:
                arr[new_next][0] = new_now

    return ''.join(answer)