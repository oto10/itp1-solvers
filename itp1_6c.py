n = int(input())
l =[[[0] * 10 for _ in range(3)] for _ in range(4)]
for i in range(n):
    b, f, r, v = map(int, input().split())
    l[b-1][f-1][r-1] += v
for i in range(4): 
    for j in range(3):
        for k in range(10):
            print(f' {l[i][j][k]}', end='')
        print()
    if i < 3:
        print('####################')
