from heapq import heappush, heappop, heapify

def part1(): # find elf with most calories
	with open('day1-1.dat')	as elfInput: # open expense items file
		items = elfInput.readlines()	# read items
		maxCal = tmp = 0
		for item in items:
			if item.strip():
				tmp += int(item.strip())
			else:
				maxCal = max(tmp, maxCal)
				tmp = 0
		print(maxCal)

part1()

def part2(): # find elf with most calories
	with open('day1-1.dat')	as elfInput: # open expense items file
		items = elfInput.readlines()	# read items
		maxCal = tmp = 0
		elves = []
		heapify(elves)
		for item in items:
			if item.strip():
				tmp += int(item.strip())
			else:
				heappush(elves, -1 * tmp)
				tmp = 0
		print(-1 * (heappop(elves) + heappop(elves) + heappop(elves)))

part2()