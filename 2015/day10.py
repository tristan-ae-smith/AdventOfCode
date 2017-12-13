puzInput = open("day10.dat").readline()	# read input seed

print puzInput

current = puzInput

for i in xrange(1,51):
	nextStr = ""
	lastChar = current[0]
	count = 0
	for c in current:
		if lastChar == c:
			count += 1
		else:
			nextStr += str(count)
			nextStr += str(lastChar)
			lastChar = c
			count = 1
	nextStr += str(count)
	nextStr += str(lastChar)
	current = nextStr
	print current
print len(current)