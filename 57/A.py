a, b, c = list(map(int, input().split()))

if a > b:
	if b > c:
		high = a
		low  = c
	else:
		high = a
		low  = b
elif b > c:
	if c > a:
		high = b
		low  = a
	else:
		high = b
		low  = c
elif c > a:
	if a > b:
		high = c
		low  = b
	else:
		high = c
		low  = a

print(low)
print(high)
