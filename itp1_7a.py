for _ in range(50):
    m, f, r = map(int, input().split())
    if m == -1 and f == -1 and r == -1:
        break
    if m == -1 or f == -1 or m + f < 30:
        print('F')
    elif 80 <= m + f:
        print('A')
    elif 65 <= m + f:
        print('B')
    elif 50 <= m + f:
        print('C')
    elif 30 <= m + f:
        if 50 <= r:
            print('C')
        else:
            print('D')