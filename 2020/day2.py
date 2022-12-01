import re

def testSpecA(spec):
	# print(spec)
	minC, maxC, charC, pwd = spec
	return int(minC) <= pwd.count(charC) <= int(maxC)

def testSpecB(spec):
	# print(spec)
	locA, locB, charC, pwd = spec
	return bool(pwd[int(locA)-1] == charC) ^ bool(pwd[int(locB)-1] == charC)

def processList(lines, specFunc):
	reg = re.compile(r"(\d+)-(\d+) (.): (.*)")
	specs = [reg.match(line).group(1,2,3,4) for line in lines]
	return sum([specFunc(spec) for spec in specs])


def test1(): # initial examples, visual inspection of output
	test = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
	print(processList(test, testSpecA))
	print(processList(test, testSpecB))


def part1(): # find matching expensesPair
	with open('day2-1.dat')	as itemInput: # open expense items file
		items = itemInput.readlines()	# read items
		print(processList(items, testSpecA))

def part2(): # find matching expensesPair
	with open('day2-1.dat')	as itemInput: # open expense items file
		items = itemInput.readlines()	# read items
		print(processList(items, testSpecB))

# test1()
# part1()
part2()