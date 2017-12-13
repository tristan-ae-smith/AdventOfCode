import re

instructions = re.compile(r't(oggle |urn o(ff |n ))(\d+),(\d+) through (\d+),(\d+)')

puzInput = open("day6.dat")	# read input seed
lights = dict.fromkeys(((x, y) for x in xrange(1000) for y in xrange(1000)), False)

for line in puzInput:
	print line[:-1],
	command = instructions.match(line).groups()
	Sx, Sy, Ex, Ey = tuple(map(int,command[2:]))
	Ex += 1 #because pytion ranges exclude end
	Ey += 1	#because python ranges are [ )
	if command[0][0] == 'o':
		print 'toggle (%d,%d) to (%d,%d)' % tuple(map(int,command[2:]))
		for i in xrange(Sx, Ex):
			for j in xrange(Sy, Ey):
				lights[(i,j)] = not lights[(i,j)]
	elif command[1][0] == 'f':
		print 'turn off (%d,%d) to (%d,%d)' % tuple(map(int,command[2:]))
		for i in xrange(Sx, Ex):
			for j in xrange(Sy, Ey):
				lights[(i,j)] = False
	else:
		print 'turn on (%d,%d) to (%d,%d)' % tuple(map(int,command[2:]))
		for i in xrange(Sx, Ex):
			for j in xrange(Sy, Ey):
				lights[(i,j)] = True

print sum(lights.values())
