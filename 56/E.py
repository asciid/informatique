from math import sqrt
x1, y1 = list(map(float, input().split()))
x2, y2 = list(map(float, input().split()))
print("{:.3f}".format(sqrt((x2 - x1)**2 + (y2 - y1)**2)))
