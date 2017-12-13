import re

vowels = re.compile('[aeiou]')
double = re.compile(r'(.)\1')
bpairs = re.compile('ab|dc|pq|xy')

puzInput = open("day5.dat")	# read input seed
nice = 0

for line in puzInput:
	print line[:-1],
	print len(vowels.findall(line)),
	print (double.search(line).group(),) if double.search(line) else "-",
	print (bpairs.search(line).group(),) if bpairs.search(line) else "-",
	if (double.search(line)) and (len(vowels.findall(line)) > 2) and not bpairs.search(line):
		print "True"
		nice += 1
	else: print "False"

print nice
