a, b = map(int, input().split())
print(a // b, a % b, round((a / b), 5))
# a / bの少数の誤差を処理しなくてはならない