from random import uniform
a, b = list(map(float, input().split()))
for x in range(0,5):
	print("{:.3f}".format(uniform(a, b)), end=' ')
print()
