"""
1. 길이가 홀 짝일때 나눠서 시작하자
2. 배치해야되는 문자열을 모두 센 다음에
3. 그 길이가 홀수면 가운데 하나 놓고 시작하고
4. 짝수면 바로 양옆에서 들어간다
"""
import sys
input = sys.stdin.readline

arr = list(map(str, input().rstrip()))
# 1. 길이가 홀 짝일때 나눠서 시작하자
ln = len(arr)
is_hansoo = True
# 홀수면
if ln % 2 == 1:
    mid = ln //2
    # 하나 빼고 짝이 맞아야 함
    check = [0] * 128
    for s in arr:
        check[ord(s)] += 1

    # 결과를 담을 리스트를 하나 만들어주고
    result = [0] * ln
    for k in range(128):
        # 홀수면 가운데 넣어주고
        if check[k] % 2 == 1:
            check[k] -= 1
            result[mid] = chr(k)
            break

    # 짝수밖에 안남은 check 을 돌면서 양 옆에 쌓아준다
    start = 0
    end = ln - 1
    for j in range(128):
        if check[j] % 2 == 1:
            print("I'm Sorry Hansoo")
            is_hansoo = False
            break
        else:
            while check[j] != 0:
                result[start] = chr(j)
                start += 1
                check[j] -= 1
                result[end] = chr(j)
                end -= 1
                check[j] -= 1

# 짝수면
else:
    # 모두 짝이 맞아야 함
    check = [0] * 128
    for s in arr:
        check[ord(s)] += 1

    # 결과를 담을 리스트를 하나 만들어주고
    result = [0] * ln

    # 짝수밖에 안남은 check 을 돌면서 양 옆에 쌓아준다
    start = 0
    end = ln - 1
    for j in range(128):
        if check[j] % 2 == 1:
            print("I'm Sorry Hansoo")
            is_hansoo = False
            break
        else:
            while check[j] != 0:
                result[start] = chr(j)
                start += 1
                check[j] -= 1
                result[end] = chr(j)
                end -= 1
                check[j] -= 1

if is_hansoo:
    str_result = ''.join(result)
    print(str_result)
