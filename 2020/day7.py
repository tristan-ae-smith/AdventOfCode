import re
from collections import defaultdict

head = re.compile(r"^([^ ]+ [^ ]+) bags contain(?: (\d+))? ([^ ]+ [^ ]+) bags?([\.,])(.*)$")
tail = re.compile(r" (\d+) ([^ ]+ [^ ]+) bags?([\.,])(.*)$")

def ruleToDict(line):
	rule = [None, None]
	finished = ''
	rest = ""
	rule[0], num, kind, finished, rest = head.match(line).groups()
	if not num:
		# print(rule)
		return rule
	rule[1] = {kind: int(num)}
	# print(rule)
	while finished != '.':
		num, kind, finished, rest = tail.match(rest).groups()
		rule[1][kind] = int(num)
		# print(rule)
	return rule

def invertRule(line):
	rule = ruleToDict(line)
	inverted = {}
	bag = rule[0]
	if not rule[1]:
		return {bag: None}
	for container in rule[1].keys():
		inverted[container] = bag
	return inverted

def processFile(fileName):
	with open(fileName) as fileInput:
		rules = fileInput.readlines()
		return rules

def findContainers(fileName):
	parentHood = defaultdict(list)
	rules = processFile(fileName)
	# print(rules)
	for rule in rules:
		contains = invertRule(rule)
		for contained, container in contains.items():
			if container:
				parentHood[contained] += [container]
	# print(parentHood)
	mine = 'shiny gold'
	candidates = parentHood[mine]
	containers = set()
	while candidates:
		# print(candidates, containers)
		test = candidates.pop()
		containers.add(test)
		candidates += parentHood[test]
	return containers

def findContained(fileName):
	rules = processFile(fileName)
	ruleDict = {}
	for rule in rules:
		bag = ruleToDict(rule)
		ruleDict[bag[0]] = bag[1]
	print(ruleDict)
	bags = ['shiny gold']
	processing = 0
	while processing < len(bags):
		toadd = ruleDict[bags[processing]]
		if not toadd:
			processing += 1
			continue
		for kind in toadd.keys():
			bags += [kind] * toadd[kind]
		# print(bags, processing)
		processing += 1
	return bags

def test1():
	print(findContainers("day7-t.dat"))

def part1():
	group = findContainers("day7-1.dat")
	print(group, len(group))

def test2():
	print(len(findContained("day7-t2.dat"))-1)

def part2():
	print(len(findContained("day7-1.dat"))-1)


# test1()
# part1()
# test2()
part2()