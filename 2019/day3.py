import sys 


grid = {}	# map of wire coordinates

dirs = {'U': (0,1), 'R': (1,0), 'D': (0,-1), 'L': (-1,0)}	# transforms for each input

test0 = [["R8","U5","L5","D3"],["U7","R6","D4","L4"]]

test1 = [["R75","D30","R83","U83","L12","D49","R71","U7","L72"],
		 ["U62","R66","U55","R34","D71","R55","D58","R83"]]

test2 = [["R98","U47","R26","D63","R33","U87","L62","D20","R33","U53","R51"],
		 ["U98","R91","D20","R16","D67","R40","U7","R15","U6","R7"]]


def writeWire(steps):
	location = (0,0)	# initial location
	step = 0
	grid[location] = True
	for segment in steps:
		dir = dirs[segment[0]] # grab the relevant transform
		dist = int(segment[1:])
		for x in range(dist):
			step += 1
			location = tuple(map(sum,zip(location, dir)))	# quick-n-dirty coordinate addition: location + transform
			grid[location] = step


def mDist(loc): # manhattan distance
	return abs(loc[0]) + abs(loc[1])

def wDist(loc, dist): # manhattan distance
	return (grid[loc] + dist) if loc in grid else sys.maxsize

def readWire(steps):
	location = (0,0)	# initial location
	cross = (sys.maxsize,sys.maxsize)

	for segment in steps:
		dir = dirs[segment[0]] # grab the relevant transform
		dist = int(segment[1:])
		for x in range(dist):
			location = tuple(map(sum,zip(location, dir)))	# quick-n-dirty coordinate addition: location + transform
			if location in grid:
				cross = location if mDist(location) < mDist(cross) else cross
	return cross

def readWire2(steps):
	location = (0,0)	# initial location
	sumW = sys.maxsize

	step = 0

	for segment in steps:
		dir = dirs[segment[0]] # grab the relevant transform
		dist = int(segment[1:])
		for x in range(dist):
			# print(step)
			step += 1
			location = tuple(map(sum,zip(location, dir)))	# quick-n-dirty coordinate addition: location + transform
			if location in grid:
				# print("potential intersection found at ", grid[location], "+", step)
				sumW = wDist(location, step) if wDist(location, step) < sumW else sumW
	return sumW

# writeWire(test2[0])
# print(mDist(readWire(test2[1])))

def part1():
	with open('day3.dat') as wInput:	# open directions file
		wires = wInput.readlines()	# read directions
		wires = [wire.strip().split(',') for wire in wires]
		# print(wires)
		writeWire(wires[0])
		print(mDist(readWire(wires[1])))

def part2():
	with open('day3.dat') as wInput:	# open directions file
		wires = wInput.readlines()	# read directions
		wires = [wire.strip().split(',') for wire in wires]
		writeWire(wires[0])
		# print(grid)
		print(readWire2(wires[1]))

part2()
