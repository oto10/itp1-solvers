while True:
    h, w = map(int, input().split())
    if h == 0 and w == 0:
        break
    for i in range(h):
        for j in range(w):
            if i % 2 == 0:
                if j % 2 == 0:
                    print('#', end='')
                else:
                    print('.', end='')
            else:
                if j % 2 == 0:
                    print('.', end='')
                else:
                    print('#', end='')
        print()
    print()

"""
i + jが偶数ならば「#」奇数ならば「.」という規則性に気が付くと, 以下のように書ける
while True:
    h, w = map(int, input().split())
    if h == 0 and w == 0:
        break
    for i in range(h):
        for j in range(w):
            if (i + j) % 2 == 0:
                print('#', end='')
            else:
                print('.', end='')
        print()
    print()
"""