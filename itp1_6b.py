n = int(input())
ls, lh, lc, ld = [], [], [], []
for i in range(n):
    s, z = input().split()
    z = int(z)
    if s == 'S':
        ls.append(z)
    if s == 'H':
        lh.append(z)
    if s == 'C':
        lc.append(z)
    if s == 'D':
        ld.append(z)
for i in range(1, 14):
    if i not in ls:
        print('S' + ' ' + str(i))
for i in range(1, 14):
    if i not in lh:
        print('H' + ' ' + str(i))
for i in range(1, 14):
    if i not in lc:
        print('C' + ' ' + str(i))
for i in range(1, 14):
    if i not in ld:
        print('D' + ' ' + str(i))