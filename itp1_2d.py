w, h, x, y, r = map(int, input().split())
if x < r or x + r > w or y < r or y + r > h:
    print('No')
else:
    print('Yes')