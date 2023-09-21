import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
keyword = set()

for _ in range(N):
    # 메모장에 적은 키워드
    keyword.add(input().rstrip())

for _ in range(M):
    # 가희가 쓴 글과 관련된 키워드가 쉼표로 구분해 주어짐
    lst = list(input().rstrip().split(','))
    for s in lst:
        keyword.discard(s)

    print(len(keyword))
