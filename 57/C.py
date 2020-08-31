age = [int(x) for x in input().split()]
names = { 'A': age[0], 'B': age[1], 'C': age[2] }
out, c = [], 0
for a, b in names.items():
	if b == max(age): out.append(a); c += 1
if c == 3:print(0)
else: print(*out)
