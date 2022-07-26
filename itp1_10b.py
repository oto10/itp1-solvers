import math
a, b, C = map(int, input().split())
C = math.radians(C)
h = b * math.sin(C)
S = (a * h) / 2
c = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(C))
L = a + b + c 
print(S, L, h, sep='\n')
