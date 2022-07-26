s = input()
p = input()
s *= 2 # 1 <= len(p) <= len(s) <= 100より, リング2周分(s*2)のみ考えれば十分
if s.find(p) == -1: # 特定の文字列の位置を取得できなければ-1を返す
    print('No')
else:
    print('Yes')