n = int(input())
t = []
h = []
t_cnt, h_cnt = 0, 0
for i in range(n):
    a, b = input().split()
    t.append(a)
    h.append(b)
for i in range(n):
    if t[i] < h[i]: # 文字列に「<」や「>」を用いると辞書順で比較した結果が返される
        h_cnt += 3
    elif t[i] == h[i]:
        t_cnt += 1
        h_cnt += 1
    else:
        t_cnt += 3
print(t_cnt, h_cnt)

"""
以下のように書いたほうが良い
n = int(input())
t_cnt = 0
h_cnt = 0
for i in range(n):
    t, h = input().split()
    if t < h:
        h_cnt += 3
    elif t == h:
        t_cnt += 1
        h_cnt += 1
    else:
        t_cnt += 3
print(t_cnt, h_cnt)
"""



