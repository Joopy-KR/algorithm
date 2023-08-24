white_paper = [[0 for j in range(100)] for i in range(100)]
counts = 0

N = int(input())

for i in range(N):
    x, y =  list(map(int, input().split()))

    for x_idx in range(x,x+10):
	    for y_idx in range(y,y+10):
             white_paper[x_idx][y_idx] = 1


for array_row in white_paper:
    counts += array_row.count(1)

print(counts)