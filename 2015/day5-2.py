import re

# vowels = re.compile('[aeiou]')
# double = re.compile(r'(.)\1')
# bpairs = re.compile('ab|dc|pq|xy')
gpairs = re.compile(r'(..).*\1')
triple = re.compile(r'(.).\1')

puzInput = open("day5.dat")	# read input seed
nice = 0

for line in puzInput:
	print line[:-1],
	# print len(vowels.findall(line)),
	# print (double.search(line).group(),) if double.search(line) else "-",
	# print (bpairs.search(line).group(),) if bpairs.search(line) else "-",
	print (gpairs.search(line).group(),) if gpairs.search(line) else "-",
	print (triple.search(line).group(),) if triple.search(line) else "-",
	if (gpairs.search(line)) and (triple.search(line)):
		print "True"
		nice += 1
	else: print "False"

print nice
