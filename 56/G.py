from random import randint
a, b = list(map(int, input().split()))
for x in range(0,5):
	print(randint(a, b), end=' ')
print()
