puzInput = open("day8.dat")	# read input seed
code = 0
newc = 0

for line in puzInput:
	i = 1
	c = 1
	n = 3
	print repr(line),

	while i < len(line)-1:
		if line[i] == '\\':
			n += 1
			if line[i+1] == '\\' :
				print 'sl',
				i += 1
				c += 1
				n += 2
			elif line[i+1] == '\"':
				print 'sp',
				i += 1
				c += 1
				n += 2
			elif line[i+1] == 'x':
				print 'he',
				i += 3
				c += 3
				n += 3
		c +=1
		n +=1
		i +=1
	n += 2 # to account for inflation of "
	print i, c, n

	code += c
	newc += n

print 'Value is (', newc, '-', code, ') =', newc - code