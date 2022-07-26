import sys

texts = sys.stdin.read() # 複数行の入力を1つの文字列として取得
texts = texts.lower()
cnt = [0] * 26
letters = 'abcdefghijklmnopqrstuvwxyz'
for x in texts:
    i = 0
    for y in letters:
        if x == y:
            cnt[i] += 1
        i += 1
for i in range(26):
    print(letters[i] + ' : ' + str(cnt[i]))
