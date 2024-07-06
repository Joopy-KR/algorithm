class SegmentTree:
    def __init__(self, data, mod):
        self.n = len(data)
        self.mod = mod
        self.tree = [1] * (2 * self.n)
        self.build(data)
        
    def build(self, data):
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = (self.tree[2 * i] * self.tree[2 * i + 1]) % self.mod

    def update(self, pos, value):
        pos += self.n
        self.tree[pos] = value
        while pos > 1:
            pos //= 2
            self.tree[pos] = (self.tree[2 * pos] * self.tree[2 * pos + 1]) % self.mod

    def query(self, left, right):
        result = 1
        left += self.n
        right += self.n + 1
        while left < right:
            if left % 2 == 1:
                result = (result * self.tree[left]) % self.mod
                left += 1
            if right % 2 == 1:
                right -= 1
                result = (result * self.tree[right]) % self.mod
            left //= 2
            right //= 2
        return result

MOD = 1000000007

# 입력 받기
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
M = int(data[1])
K = int(data[2])

array = [int(data[i]) for i in range(3, 3 + N)]
operations = data[3 + N:]

# 구간 트리 초기화
seg_tree = SegmentTree(array, MOD)

# 연산 수행
index = 0
output = []
while index < len(operations):
    a = int(operations[index])
    b = int(operations[index + 1])
    c = int(operations[index + 2])
    if a == 1:
        seg_tree.update(b - 1, c)
    elif a == 2:
        result = seg_tree.query(b - 1, c - 1)
        output.append(result)
    index += 3

# 결과 출력
sys.stdout.write('\n'.join(map(str, output)) + '\n')
