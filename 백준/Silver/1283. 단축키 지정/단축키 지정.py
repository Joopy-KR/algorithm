import sys
input = sys.stdin.readline

N = int(input())
keyword = {chr(i): False for i in range(65, 91)}
for _ in range(N):
    words = input().rstrip().split()
    is_continue = True
    if len(words) == 0:
        break
    # 첫글자 검사
    for idx in range(len(words)):
        if not keyword[words[idx][0].upper()]:  # 첫글자가 키워드라면 변환 후 break
            keyword[words[idx][0].upper()] = True
            words[idx] = f"[{words[idx][0]}]{words[idx][1:]}"
            is_continue = False
            break

    # 첫글자 검사에 실패했다면 알파벳검사
    if is_continue:
        is_is_continue = True
        for idx2 in range(len(words)):
            if not is_is_continue:
                break
            for idx3 in range(len(words[idx2])):
                if not keyword[words[idx2][idx3].upper()]:
                    keyword[words[idx2][idx3].upper()] = True
                    words[idx2] = words[idx2][:idx3] + f"[{words[idx2][idx3]}]" + words[idx2][idx3+1:]
                    is_is_continue = False
                    break

    for answer in words:
        print(answer, end=" ")
    print()
