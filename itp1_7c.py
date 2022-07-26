r, c = map(int, input().split())
l = [list(map(int, input().split())) for i in range(r)]
for i in range(r): # 各行の合計値を計算してリストに追加
    l[i].append(sum(l[i]))
c_sum = [0] * (c + 1) # 要素0がc + 1個のリスト
for j in range(c + 1): # 新たに追加した列の合計値も求める
    for k in range(r):
        c_sum[j] += l[k][j]
for i in range(r):
    print(*l[i])
print(*c_sum)