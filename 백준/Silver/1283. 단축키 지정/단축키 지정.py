import sys
input = sys.stdin.readline


def is_inaskii(wrd: str) -> bool:
    global askii_dict
    if wrd.isupper():
        if askii_dict[ord(wrd)] or askii_dict[ord(wrd) + 32]:
            return True
        else:
            return False
    else:
        if askii_dict[ord(wrd)] or askii_dict[ord(wrd) - 32]:
            return True
        else:
            return False


def change_option(opt: str, idx_: int):
    return opt[:idx_] + f"[{opt[idx_]}]" + opt[idx_ + 1:]


def add_shortcut(opt:str, changed_opt: str):
    global shortcut_dict
    shortcut_dict[opt] = changed_opt


def add_askii(wrd: str):
    global askii_dict
    if wrd.isupper():
        askii_dict[ord(wrd)] = True
        askii_dict[ord(wrd) + 32] = True
    else:
        askii_dict[ord(wrd)] = True
        askii_dict[ord(wrd) - 32] = True


N = int(input().rstrip())
shortcut_dict = dict()
askii_dict = {i: False for i in range(65, 123)}
# 65~90 대문자 / 97~122 소문자
for _ in range(N):
    option = input().rstrip()
    if option in shortcut_dict:  # 단어가 있는지 검사
        print(shortcut_dict[option])
        continue

    for idx in range(len(option)):  # 첫번째 단어 검사
        if len(option) > 1:
            if idx == 0:  # 첫 단어 검사
                if askii_dict[ord(option[idx])]:
                    continue
                changed_option = change_option(option, idx)
                add_shortcut(option, changed_option)
                add_askii(option[idx])
                print(changed_option)
                break
            else:
                if option[idx - 1] == " ":  # 두 번째 단어부터 검사
                    if askii_dict[ord(option[idx])]:
                        continue
                    changed_option = change_option(option, idx)
                    add_shortcut(option, changed_option)
                    add_askii(option[idx])
                    print(changed_option)
                    break
        else:  # 옵션이 한 글자인 경우 (이미 등록되어 있다면 아래를 수행할 필요 없음)
            if askii_dict[ord(option)]:
                print(option)
                break
            else:
                changed_option = change_option(option, 0)
                add_shortcut(option, changed_option)
                add_askii(option[idx])
                print(changed_option)
                break

    else:  # 첫 글자 검색에서 없었으면 알파벳 검색
        for idx2 in range(len(option)):
            alphabet = option[idx2]
            if alphabet == " ":
                continue
            if askii_dict[ord(alphabet)]:
                continue
            changed_option = change_option(option, idx2)
            add_shortcut(option, changed_option)
            add_askii(option[idx2])
            print(changed_option)
            break
        else:  # 그래도 없으면 그냥 출력
            print(option)
