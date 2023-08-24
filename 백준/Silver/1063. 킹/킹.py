"""
0. 체스판의 범위 내에서 (나가면 건너뜀)
1. 커맨드 함수에 움직일 방향을 다 넣어주고
2. 만약 움직인 곳 위치가 돌 위치와 같다면
3. 체스판의 범위 내에서 (나가면 건너뜀)
4. 돌도 동일하게 움직여준다.

ASKII
A = 65
H = 72
"""
import sys
input = sys.stdin.readline


# 1. 커맨드 함수에 움직일 방향을 다 넣어주고
def command(order):
    if order == 'R':
        # 0. 체스판의 범위 내에서 (나가면 건너뜀)
        if ord(king[0]) + 1 <= 72:
            king[0] = chr(ord(king[0]) + 1)
            # 2. 만약 움직인 곳 위치가 돌 위치와 같다면
            if king == stone:
                # 3. 체스판의 범위 내에서 (나가면 건너뜀)
                if ord(stone[0]) + 1 <= 72:
                    # 4. 돌도 동일하게 움직여준다.
                    stone[0] = chr(ord(stone[0]) + 1)
                # 나가면 킹도 원상복구
                else:
                    king[0] = chr(ord(king[0]) - 1)
    if order == 'L':
        # 0. 체스판의 범위 내에서 (나가면 건너뜀)
        if 65 <= ord(king[0]) - 1:
            king[0] = chr(ord(king[0]) - 1)
            # 2. 만약 움직인 곳 위치가 돌 위치와 같다면
            if king == stone:
                # 3. 체스판의 범위 내에서 (나가면 건너뜀)
                if 65 <= ord(stone[0]) - 1:
                    # 4. 돌도 동일하게 움직여준다.
                    stone[0] = chr(ord(stone[0]) - 1)
                # 나가면 킹도 원상복구
                else:
                    king[0] = chr(ord(king[0]) + 1)
    if order == 'B':
        # 0. 체스판의 범위 내에서 (나가면 건너뜀)
        if 1 <= int(king[1]) - 1:
            king[1] = str(int(king[1]) - 1)
            # 2. 만약 움직인 곳 위치가 돌 위치와 같다면
            if king == stone:
                # 3. 체스판의 범위 내에서 (나가면 건너뜀)
                if 1 <= int(stone[1]) - 1:
                    # 4. 돌도 동일하게 움직여준다.
                    stone[1] = str(int(stone[1]) - 1)
                # 나가면 킹도 원상복구
                else:
                    king[1] = str(int(king[1]) + 1)
    if order == 'T':
        # 0. 체스판의 범위 내에서 (나가면 건너뜀)
        if int(king[1]) + 1 <= 8:
            king[1] = str(int(king[1]) + 1)
            # 2. 만약 움직인 곳 위치가 돌 위치와 같다면
            if king == stone:
                # 3. 체스판의 범위 내에서 (나가면 건너뜀)
                if int(stone[1]) + 1 <= 8:
                    # 4. 돌도 동일하게 움직여준다.
                    stone[1] = str(int(stone[1]) + 1)
                # 나가면 킹도 원상복구
                else:
                    king[1] = str(int(king[1]) - 1)
    if order == 'RT':
        # 0. 체스판의 범위 내에서 (오른쪽 위)
        if ord(king[0]) + 1 <= 72 and int(king[1]) + 1 <= 8:
            king[0] = chr(ord(king[0]) + 1)
            king[1] = str(int(king[1]) + 1)
            # 2. 만약 움직인 곳 위치가 돌 위치와 같다면
            if king == stone:
                # 3. 체스판의 범위 내에서 (나가면 건너뜀)
                if ord(stone[0]) + 1 <= 72 and int(stone[1]) + 1 <= 8:
                    # 4. 돌도 동일하게 움직여준다.
                    stone[0] = chr(ord(stone[0]) + 1)
                    stone[1] = str(int(stone[1]) + 1)
                # 나가면 킹도 원상복구
                else:
                    king[0] = chr(ord(king[0]) - 1)
                    king[1] = str(int(king[1]) - 1)
    if order == 'LT':
        # 0. 체스판의 범위 내에서 (오른쪽 위)
        if 65 <= ord(king[0]) - 1 and int(king[1]) + 1 <= 8:
            king[0] = chr(ord(king[0]) - 1)
            king[1] = str(int(king[1]) + 1)
            # 2. 만약 움직인 곳 위치가 돌 위치와 같다면
            if king == stone:
                # 3. 체스판의 범위 내에서 (나가면 건너뜀)
                if 65 <= ord(stone[0]) - 1 and int(stone[1]) + 1 <= 8:
                    # 4. 돌도 동일하게 움직여준다.
                    stone[0] = chr(ord(stone[0]) - 1)
                    stone[1] = str(int(stone[1]) + 1)
                # 나가면 킹도 원상복구
                else:
                    king[0] = chr(ord(king[0]) + 1)
                    king[1] = str(int(king[1]) - 1)
    if order == 'RB':
        # 0. 체스판의 범위 내에서 (오른쪽 위)
        if ord(king[0]) + 1 <= 72 and 1 <= int(king[1]) - 1:
            king[0] = chr(ord(king[0]) + 1)
            king[1] = str(int(king[1]) - 1)
            # 2. 만약 움직인 곳 위치가 돌 위치와 같다면
            if king == stone:
                # 3. 체스판의 범위 내에서 (나가면 건너뜀)
                if ord(stone[0]) + 1 <= 72 and 1 <= int(stone[1]) - 1:
                    # 4. 돌도 동일하게 움직여준다.
                    stone[0] = chr(ord(stone[0]) + 1)
                    stone[1] = str(int(stone[1]) - 1)
                # 나가면 킹도 원상복구
                else:
                    king[0] = chr(ord(king[0]) - 1)
                    king[1] = str(int(king[1]) + 1)
    if order == 'LB':
        # 0. 체스판의 범위 내에서 (오른쪽 위)
        if 65 <= ord(king[0]) - 1 and 1 <= int(king[1]) - 1:
            king[0] = chr(ord(king[0]) - 1)
            king[1] = str(int(king[1]) - 1)
            # 2. 만약 움직인 곳 위치가 돌 위치와 같다면
            if king == stone:
                # 3. 체스판의 범위 내에서 (나가면 건너뜀)
                if 65 <= ord(stone[0]) - 1 and 1 <= int(stone[1]) - 1:
                    # 4. 돌도 동일하게 움직여준다.
                    stone[0] = chr(ord(stone[0]) - 1)
                    stone[1] = str(int(stone[1]) - 1)
                # 나가면 킹도 원상복구
                else:
                    king[0] = chr(ord(king[0]) + 1)
                    king[1] = str(int(king[1]) + 1)


arr = list(map(list, input().rstrip().split()))
king = arr[0]
stone = arr[1]
N = int(''.join(arr[2]))
for _ in range(int(N)):
    order = input().rstrip()
    command(order)

result_king = ''.join(king)
result_stone = ''.join(stone)
print(result_king)
print(result_stone)