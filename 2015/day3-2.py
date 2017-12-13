#!/usr/bin/python


houses = {}
robo = True		# flag for referring to robo-santa
location = {True:(0,0), False:(0,0)}	# store two locations indexed by flag
dirs = {'^': (0,1), '>': (1,0), 'v': (0,-1), '<': (-1,0)}	# coordinate transforms

instring = open('day3.dat').read()	# condensed file reading
houses[location[robo]] = True		# store initial location
for c in instring:
	location[robo] = tuple(map(sum,zip(location[robo], dirs[c]))) # transform location of current santa
	houses[location[robo]] = True	# store location of current santa
	robo = not robo					# refer to other santa
print len(houses)