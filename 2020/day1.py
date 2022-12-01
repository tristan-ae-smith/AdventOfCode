def expensesPair(list):
	list.sort()
	while(list):
		item = list.pop(0)
		for other in list:
			if item + other == 2020:
				return item * other
	return

def expensesTrio(list):
	list.sort()
	# print(list)
	while(list):
		first = list.pop(0)
		# print("f",first)
		for second in list:
			# print("s",second)
			if first + second + second > 2020:
				break
			for third in list:
				# print("t",third)
				if third == second:
					continue
				if first + second + third == 2020:
					return first * second * third
	return

def test1(): # initial examples, visual inspection of output
	test = [1721, 979, 366, 299, 675, 1456]
	print(expensesPair(test))
	print(expensesTrio(test))


def part1(): # find matching expensesPair
	with open('day1-1.dat')	as itemInput: # open expense items file
		items = itemInput.readlines()	# read items
		items = [int(item.strip()) for item in items]
		print(expensesPair(items))

def part2(): # find matching expensesPair
	with open('day1-1.dat')	as itemInput: # open expense items file
		items = itemInput.readlines()	# read items
		items = [int(item.strip()) for item in items]
		print(expensesTrio(items))

# test1()
# part1()
part2()