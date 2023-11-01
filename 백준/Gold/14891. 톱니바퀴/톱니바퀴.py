"""
1. 기어를 돌리고
2. 붙어 있는 기어(1이면 2 / 2면 1, 3 / 3이면 2, 4 / 4면 3)의 [2] 를 확인한다
3. 만약 극이 다르면 회전시키고 방향 기록하고 넘어간다
4. 만약 극이 같으면 방향에 0 체크하고 넘어간다
5. 만약 방향이 왔으면 반대로 돌리고, 0이 왔으면 break
6. K번 다 돌았으면 상태를 확인한다.
"""
from collections import deque
import sys
input = sys.stdin.readline

gear1 = deque(map(int, input().rstrip()))
gear2 = deque(map(int, input().rstrip()))
gear3 = deque(map(int, input().rstrip()))
gear4 = deque(map(int, input().rstrip()))


K = int(input().rstrip())

# arr[2]가 다르면 회전, 같으면 안회전
for _ in range(K):
    # W: 어느 바퀴를 R: 어디로 돌렸냐 (1. 시계  2. 반시계)
    W, R = map(int, input().rstrip().split())
    before = 0

    # 1. 기어를 돌리고
    # 1번 기어일때
    if W == 1:
        # 돌리기 전에 기어 저장해두기 (1번 기어의 오른쪽)
        before = gear1[2]
        # 시계 방향(오른쪽)으로 돌리기
        if R == 1:
            gear1.rotate(1)
        # 반시계 방향(왼쪽)으로 돌리기
        elif R == -1:
            gear1.rotate(-1)
        # 1번일때 2번 기어가 돌아가므로 2번 기어 왼쪽 확인하기
        # 같다면(안돌아간다면)
        if before == gear2[6]:
            # 이하 코드 실행하지 않음
            continue
        # 다르다면(돌아간다면)
        else:
            before = gear2[2]
            # 시계방향으로 돌아갔다면
            if R == 1:
                # 반시계로 돌리기
                gear2.rotate(-1)
            # 반시계로 돌아갔다면
            elif R == -1:
                # 시계로 돌리기
                gear2.rotate(1)
                # 3번 기어 확인하기
            if before == gear3[6]:
                # 이하 코드 실행 안함
                continue
            else:
                # 저장해두고
                before = gear3[2]
                # 1번과 같은 방향으로
                if R == 1:
                    gear3.rotate(1)
                elif R == -1:
                    gear3.rotate(-1)
                # 4번 기어 확인하기
                if before == gear4[6]:
                    continue
                # 2번 기어랑 같은 방향으로
                else:
                    if R == 1:
                        gear4.rotate(-1)
                    elif R == -1:
                        gear4.rotate(1)
    # 2번 기어일때 (2면 1, 3)
    elif W == 2:
        # 1번 기어부터 확인하기
        before = gear2[6]
        # 시계 방향으로 돌리기
        if R == 1:
            gear2.rotate(1)
        elif R == -1:
            gear2.rotate(-1)
        # 1번 기어 확인하기
        if before == gear1[2]:
            # 2번 기어가 시계 방향으로 돌아갔었다면(2번이 3번이 됨)
            if R == 1:
                before = gear2[3]
            # 2번이 1번이 됨
            elif R == -1:
                before = gear2[1]
        else:
            # 여기서 before는 다음에 3번기어 봐야하므로 gear2의 2번(이었던 것)을 봐야됨!!!
            # 2번 기어 반대로 돌리기
            if R == 1:
                before = gear2[3]
                gear1.rotate(-1)
            elif R == -1:
                before = gear2[1]
                gear1.rotate(1)
        # 3번 기어 1번 기어 확인과 상관없음!!!!!!!
        # 3번 기어 확인하기
        if before == gear3[6]:
            continue
        else:
            before = gear3[2]
            # 1번과 같은 방향으로 돌리기
            if R == 1:
                gear3.rotate(-1)
            elif R == -1:
                gear3.rotate(1)
            # 4번 기어 확인하기
            if before == gear4[6]:
                continue
            else:
                # 2번과 같은 방향으로 돌리기
                # 시계 방향으로 돌리기
                if R == 1:
                    gear4.rotate(1)
                elif R == -1:
                    gear4.rotate(-1)
    # 3번 기어일때 (3이면 2, 4)
    elif W == 3:
        # 4번 기어부터 확인하기
        before = gear3[2]
        # 시계 방향으로 돌리기
        if R == 1:
            gear3.rotate(1)
        elif R == -1:
            gear3.rotate(-1)
        # 4번 기어 확인하기
        if before == gear4[6]:
            # 3번 기어가 시계 방향으로 돌아갔었다면(6번이 7번이 됨)
            if R == 1:
                before = gear3[7]
            # 6번이 5번이 됨
            elif R == -1:
                before = gear3[5]
        else:
            # 여기서 before는 다음에 2번 봐야 하므로 gear3의 6번 이었던 것이 됨
            # 3번 기어 반대로 돌리기
            if R == 1:
                before = gear3[7]
                gear4.rotate(-1)
            elif R == -1:
                before = gear3[5]
                gear4.rotate(1)
        # 2번 기어 4번 기어 확인과 상관없음!!!!!!!
        # 2번 기어 확인하기
        if before == gear2[2]:
            continue
        else:
            before = gear2[6]
            # 4번과 같은 방향으로 돌리기
            if R == 1:
                gear2.rotate(-1)
            elif R == -1:
                gear2.rotate(1)
            # 1번 기어 확인하기
            if before == gear1[2]:
                continue
            else:
                if R == 1:
                    gear1.rotate(1)
                elif R == -1:
                    gear1.rotate(-1)
    # 4번 기어일때 (4번이면 3) (왼쪽으로만 가야됨 - 이전것의 6과 다음 기어의 2를 비교할것)
    elif W == 4:
        # 기어 저장
        before = gear4[6]
        # 시계 방향(오른쪽)으로 돌리기
        if R == 1:
            gear4.rotate(1)
        # 반시계 방향(왼쪽)으로 돌리기
        elif R == -1:
            gear4.rotate(-1)
        # 3번 기어 확인하기
        # 같다면(안돌아간다면)
        if before == gear3[2]:
            # 이하 코드 실행하지 않음
            continue
        else:
            before = gear3[6]
            # 시계방향으로 돌아갔다면
            if R == 1:
                # 반시계로 돌리기
                gear3.rotate(-1)
            # 반시계로 돌아갔다면
            elif R == -1:
                # 시계로 돌리기
                gear3.rotate(1)
            # 2번 기어 확인하기
            if before == gear2[2]:
                continue
            else:
                before = gear2[6]
                # 4번과 같은 방향으로
                if R == 1:
                    gear2.rotate(1)
                elif R == -1:
                    gear2.rotate(-1)
                # 1번 기어 확인
                if before == gear1[2]:
                    continue
                else:
                    if R == 1:
                        gear1.rotate(-1)
                    elif R == -1:
                        gear1.rotate(1)

result = 0

# N극: 0 / S극: 1
if gear1[0] == 1:
    result += 1
if gear2[0] == 1:
    result += 2
if gear3[0] == 1:
    result += 4
if gear4[0] == 1:
    result += 8

print(result)