# Right 1, down 1.
# Right 3, down 1. (This is the slope you already checked.)
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.

def countTreesx1(forest,x):
	cols = len(forest[0])
	xVal, trees = 0, 0
	for row in forest:
		trees += row[xVal]=='#'
		xVal = (xVal+x) % cols
	return trees

def countTreesx2(forest,x):
	cols = len(forest[0])
	xVal, trees = 0, 0
	skip = False
	for row in forest:
		if skip:
			skip = False
			continue
		trees += row[xVal]=='#'
		xVal = (xVal+x) % cols
		skip = True
	return trees

def getForest(file):
	with open(file)	as treeInput: # open forest map file
		forest = treeInput.readlines()	# read items
		forest = [tree.strip() for tree in forest]
		return forest

def test1():
	print(countTreesx1(getForest('day3-t.dat'),3))


def part1():
	print(countTreesx1(getForest('day3-1.dat'),3))

def test2():
	forest = getForest('day3-t.dat')
	print(countTreesx1(forest,1) *
		  countTreesx1(forest,3) *
		  countTreesx1(forest,5) *
		  countTreesx1(forest,7) *
		  countTreesx2(forest,1))

def part2():
	forest = getForest('day3-1.dat')
	print(countTreesx1(forest,1) *
		  countTreesx1(forest,3) *
		  countTreesx1(forest,5) *
		  countTreesx1(forest,7) *
		  countTreesx2(forest,1))

# test1()
# part1()
# test2()
part2()