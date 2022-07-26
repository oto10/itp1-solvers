text = input()
n = int(input())
for i in range(n):
    s = input().split()
    a, b = map(int, s[1:3])
    if s[0] == 'print':
        print(text[a:b+1])
    elif s[0] == 'reverse':
        tmp = text[a:b+1]
        text = text[:a] + tmp[::-1] + text[b+1:]
    else:
        text = text[:a] + s[3] + text[b+1:]
