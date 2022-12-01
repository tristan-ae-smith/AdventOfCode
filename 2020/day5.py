rows, cols = 128, 8

def seatID(row, col):
	return row*8 +col

def haf(x):
	return x//2

def mid(x, y):
	return (x+y)//2

def locate(string):
	bounds = {'xmin': 0, 'ymin':0, 'xmax': cols-1, 'ymax': rows-1}
	for char in string:
		if char == 'F':
			bounds['ymax'] = mid(bounds['ymin'], bounds['ymax'])
		elif char == 'B':
			bounds['ymin'] = mid(bounds['ymin'], bounds['ymax']) + 1
		elif char == 'L':
			bounds['xmax'] = mid(bounds['xmin'], bounds['xmax'])
		elif char == 'R':
			bounds['xmin'] = mid(bounds['xmin'], bounds['xmax']) + 1
		else:
			print('what')
		# print (bounds)
	if bounds['ymin'] == bounds['ymax'] and bounds['xmin'] == bounds['xmax']:
		return (bounds['ymax'], bounds['xmax'])
	print('huh')

def readFile(fileName):
	with open(fileName) as inputFile:
		passes = inputFile.readlines()
		passes = [line.strip() for line in passes]
		return passes

def test1():
	print(seatID(*locate("FBFBBFFRLR")))
	print(seatID(*locate("BFFFBBFRRR")))
	print(seatID(*locate("FFFBBBFRRR")))
	print(seatID(*locate("BBFFBBFRLL")))

def part1():
	passes = readFile("day5-1.dat")
	ids = [seatID(*locate(passString)) for passString in passes]
	print(max(ids))

def part2():
	seats = [[False for _ in range(cols)] for _ in range (rows)]
	passes = readFile("day5-1.dat")
	for passString in passes:
		row, col = locate(passString)
		# print(row, col)
		seats[row][col] = True
	print(seats)
	found = False
	seat = [0,0]
	for y in range(rows):
		for x in range(cols):
			if found: #if the previous seat existed, update our guess
				seat = [y, x]
			elif not found and seats[y][x] and seat[0]: #if the previous seat was not filled and this one is and we have a guess
				break
			found = seats[y][x] #update seat existence
		if not found and seat[0]:
			break
	print(seat[0], seat[1], seatID(seat[0], seat[1]))


# test1()
# part1()
part2()