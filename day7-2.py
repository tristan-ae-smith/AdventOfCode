import re

instructions = re.compile(r'(\w+)?? ?(NOT|AND|OR|RSHIFT|LSHIFT)? ?(\w+) -> (\w+)')

puzInput = open("day7.dat")	# read input seed
sources = {}
values = {}

def getVal(x):
	if x in values.keys():
		return values[x]
	return int(x)

for line in puzInput:
	print line[:-1],
	command = instructions.match(line).groups() # split the important elements
	print command
	sources[command[3]] = command[:3] # associate a wire with it's source
	values[command[3]] = None if command[1] else int(command[2]) # record existence of wire, with given value if no operator

print sources
print values

# for part 2
values['b'] = 956

while None in values.values():
	for wire in (emptywire for emptywire in values if None == values[emptywire]):
		second = getVal(sources[wire][2])
		if None == second:
			continue		#early out if we are missing a value

		command = sources[wire][1]

		if command[0] == 'N':
			print 'new value for', wire, 'is negation of', sources[wire][2], second, ~second
			values[wire] = ~second	# negate variable and store as value
			continue

		first = getVal(sources[wire][0])
		if None == first:
			continue		#early-ish out if we are missing a value

		if command[0] == 'A':
			print 'new value for', wire, 'is addition of', sources[wire][0], first, 'and', sources[wire][2], second, ':', first & second
			values[wire] = first & second
			continue
		elif command[0] == 'O':
			print 'new value for', wire, 'is or of', sources[wire][0], first, 'and', sources[wire][2], second, ':', first | second
			values[wire] = first | second
			continue
		elif command[0] == 'R':
			print 'new value for', wire, 'is rshift of', sources[wire][0], first, 'and', second, ':', first >> second
			values[wire] = first >> second
			continue
		elif command[0] == 'L':
			print 'new value for', wire, 'is lshift of', sources[wire][0], first, 'and', second, ':', first << second
			values[wire] = first << second
			continue

print sources
print values

print 'Value of a is', values['lx'] # day7.dat was originally mangled with addition of 'lx -> a' rule. Easier to read that than code exception in parser