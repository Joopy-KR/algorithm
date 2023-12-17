import sys
input = sys.stdin.readline

while True:
    arr = list(map(str, input().rstrip()))

    if arr == ['.']:
        break
    else:
        stack = []

        for i in range(len(arr)):
            if arr[i] == '(':
                stack.append(arr[i])
            elif arr[i] == ')':
                if stack:
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        print('no')
                        break
                else:
                    print('no')
                    break
            elif arr[i] == '[':
                stack.append(arr[i])
            elif arr[i] == ']':
                if stack:
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        print('no')
                        break
                else:
                    print('no')
                    break
        else:
            if stack:
                print('no')
            else:
                print('yes')
