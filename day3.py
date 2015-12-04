#!/usr/bin/python


houses = {}	# map of house coordinates
location = (0,0)	# initial location
dirs = {'^': (0,1), '>': (1,0), 'v': (0,-1), '<': (-1,0)}	# transforms for each input

dirinput = open('day3.dat')	# open directions file
instring = dirinput.read()	# read directions
houses[location] = True		# store first house
for c in instring:			# for each character direcion
	location = tuple(map(sum,zip(location, dirs[c])))	# quick-n-dirty coordinate addition: location + transform
	houses[location] = True	# store new location
print len(houses)			# print output once done
