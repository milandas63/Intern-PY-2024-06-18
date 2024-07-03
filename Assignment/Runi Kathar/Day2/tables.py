def padL(n, l):
	r = str(n)
	for i in range(len(r),l):
		r=''+r
		return r
start = 2
end = 10
for i in range(start, end+1, 5):
	for j in range(1, 11):
		for k in range(i, i+5):
			print(k," x ",j," = ",(k*j), end="  ")
		print()
	print()
print()