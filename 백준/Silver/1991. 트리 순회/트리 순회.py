def preorder(n):
    global pre_result
    if n:
        pre_result += chr(n)
        preorder(ch1[n])
        preorder(ch2[n])
    return pre_result

def inorder(n):
    global in_result
    if n:
        inorder(ch1[n])
        in_result += chr(n)
        inorder(ch2[n])
    return in_result

def postorder(n):
    global post_result
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        post_result += chr(n)
    return post_result

N = int(input())
ch1 = [0] * 1000
ch2 = [0] * 1000
pre_result = ''
in_result = ''
post_result = ''

for _ in range(N):
    p, c1, c2 = map(str, input().split())
    if c1 != '.':
        ch1[ord(p)] = ord(c1)
    if c2 != '.':
        ch2[ord(p)] = ord(c2)

print(preorder(ord('A')))
print(inorder(ord('A')))
print(postorder(ord('A')))
