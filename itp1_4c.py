while True:
    a, op, b = input().split()
    a, b = int(a), int(b)
    if op == '+':
        print(a + b)
    if op == '-':
        print(a - b)
    if op == '*':
        print(a * b)
    if op == '/':
        print(a // b)
    if op == '?':
        break
