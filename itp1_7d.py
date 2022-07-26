n, m, l = map(int, input().split())
A = [list(map(int, input().split())) for i in range(n)]
B = [list(map(int, input().split())) for i in range(m)]
for i in range(n):
    ans = []
    for j in range(l):
        c = 0 
        for k in range(m):
            c += A[i][k] * B[k][j]
        ans.append(c)
    print(*ans)