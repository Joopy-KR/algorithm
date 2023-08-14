import sys
input = sys.stdin.readline

tag = ['<', '>']
S = input().rstrip()

# 태그가 있을때
if '<' in S:
    idx = -1
    result_str = ''
    temp_str = ''
    while idx < len(S) - 1:
        idx += 1
        if S[idx] == '<':
            result_str += temp_str[::-1]
            temp_str = ''
            while S[idx] != '>':
                result_str += S[idx]
                idx += 1
            result_str += '>'
        elif S[idx] == ' ':
            result_str += temp_str[::-1]
            temp_str = ''
            result_str += S[idx]
        else:
            if S[idx] == '<':
                result_str += temp_str[::-1]
                temp_str = ''
            elif S[idx] == ' ':
                result_str += temp_str[::-1]
                temp_str = ''
            else:
                temp_str += S[idx]
    result_str += temp_str[::-1]
    temp_str = ''
    print(result_str)

# 태그가 없을때
else:
    arr = list(map(str, S.split()))
    for i in range(len(arr)):
        arr[i] = arr[i][::-1]
    result = ' '.join(arr)
    print(result)