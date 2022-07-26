import sys

w = input()
t = sys.stdin.read()
print(t.lower().split().count(w))