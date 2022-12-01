
def part1(orbits):
	oCount = 0
	for obj in orbits:
		print("dir:", obj)
		oCount += 1
		o = orbits[obj]
		while o != 'COM':
			print("ind:", o)
			oCount += 1
			o = orbits[o]

	print(oCount)



def part2(orbits):
	you = []
	y = orbits['YOU']
	while y != 'COM':
		you += [y]
		y = orbits[y]
	print(you)

	san = []
	s = orbits['SAN']
	while s != 'COM':
		san += [s]
		s = orbits[s]
	print(san)

	while you[-1] == san[-1]:
		you.pop()
		san.pop()
	print(you)
	print(san)
	print(len(you) + len(san))

with open('day6.dat')	as intInput: # open orbits file
	orbits = intInput.readlines()	# read orbits
	orbits = [orbit.strip().split(')') for orbit in orbits]
	orbits = {orbit[1]:orbit[0] for orbit in orbits}
	# print(orbits)
	# part1(orbits)
	part2(orbits)