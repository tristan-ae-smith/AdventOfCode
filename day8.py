puzInput = open("day8.dat")	# read input seed
code = 0
rawm = 0

for line in puzInput:
	i = 1
	c = 1
	r = 0
	print repr(line),

	while i < len(line)-1:
		if line[i] == '\\':
			if line[i+1] == '\\' :
				print 'sl',
				i += 1
				c += 1
			elif line[i+1] == '\"':
				print 'sp',
				i += 1
				c += 1
			elif line[i+1] == 'x':
				print 'he',
				i += 3
				c += 3
		c +=1
		r +=1
		i +=1
	r -= 1 # ignore terminating "
	print i, c, r

	code += c
	rawm += r

print 'Value is (', code, '-', rawm, ') =', code - rawm