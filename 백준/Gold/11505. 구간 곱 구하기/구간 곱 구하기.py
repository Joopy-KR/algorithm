import sys
input = sys.stdin.readline

MOD = 1000000007

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [1] * (4 * self.n)
        self.build(arr, 1, 0, self.n - 1)

    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start] % MOD
        else:
            mid = (start + end) // 2
            self.build(arr, node * 2, start, mid)
            self.build(arr, node * 2 + 1, mid + 1, end)
            self.tree[node] = (self.tree[node * 2] * self.tree[node * 2 + 1]) % MOD

    def update(self, node, start, end, index, value):
        if index < start or index > end:
            return
        if start == end:
            self.tree[node] = value % MOD
        else:
            mid = (start + end) // 2
            self.update(node * 2, start, mid, index, value)
            self.update(node * 2 + 1, mid + 1, end, index, value)
            self.tree[node] = (self.tree[node * 2] * self.tree[node * 2 + 1]) % MOD

    def query(self, node, start, end, left, right):
        if left > end or right < start:
            return 1
        if left <= start and end <= right:
            return self.tree[node]
        mid = (start + end) // 2
        return (self.query(node * 2, start, mid, left, right) * 
                self.query(node * 2 + 1, mid + 1, end, left, right)) % MOD

# 입력 처리
N, M, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

# 세그먼트 트리 생성
seg_tree = SegmentTree(arr)

# 쿼리 처리
for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:  # 업데이트 쿼리
        seg_tree.update(1, 0, N - 1, b - 1, c)
    else:  # 곱 쿼리
        print(seg_tree.query(1, 0, N - 1, b - 1, c - 1))