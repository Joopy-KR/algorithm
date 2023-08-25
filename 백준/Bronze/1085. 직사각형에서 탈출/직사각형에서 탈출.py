x, y, w, h = map(int, input().split())

min_length = 2000
to_left = x
if min_length > to_left:
    min_length = to_left

to_right = w - x
if min_length > to_right:
    min_length = to_right

to_down = y
if min_length > to_down:
    min_length = to_down

to_up = h - y
if min_length > to_up:
    min_length = to_up

print(min_length)