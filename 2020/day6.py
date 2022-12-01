# import string
# tally = dict.fromkeys(string.ascii_lowercase, False)
from collections import defaultdict

def processGroupAny(group):
	groupCount = {}
	for person in group:
		for answer in person:
			groupCount[answer] = True
	# print(groupCount)
	return sum(groupCount.values())

def processGroupAll(group):
	groupCount = defaultdict(int)
	for person in group:
		for answer in person:
			groupCount[answer] += 1
	print(groupCount, len(group))
	return sum([groupCount[key] == len(group) for key in groupCount.keys()])


def fileToSets(filename):
	with open(filename)	as fileInput: # open expense items file
		lines = fileInput.readlines()	# read items
		lines = [line.strip() for line in lines]
		acc = []
		items = []
		while lines:
			item = lines.pop(0)
			if not item:
				items += [acc]
				acc = []
				continue
			acc += [item]
		items += [acc]
		return items

def test1():
	answers = fileToSets("day6-t.dat")
	print(sum(map(processGroupAny, answers)))

def part1():
	answers = fileToSets("day6-1.dat")
	print(sum(map(processGroupAny, answers)))

def test2():
	answers = fileToSets("day6-t.dat")
	print(sum(map(processGroupAll, answers)))

def part2():
	answers = fileToSets("day6-1.dat")
	print(sum(map(processGroupAll, answers)))

# test1()
# part1()
# test2()
part2()

