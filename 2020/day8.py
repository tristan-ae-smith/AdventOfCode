import re
from collections import defaultdict

reg = re.compile(r"(\w\w\w) ([-|+]\d+)")

accx = int()
indx = int()
trak = defaultdict(lambda:False)

def nop(value):
	global indx
	indx += 1

def acc(value):
	global accx 
	global indx
	accx += value
	indx += 1

def jmp(value):
	global indx
	indx += value

run = {"nop": nop, "acc": acc, "jmp": jmp}

def processFile(fileName):
	with open(fileName) as fileInput:
		instructions = fileInput.readlines()
		instructions = [list(reg.match(inst).groups()) for inst in instructions]
		print(instructions)
		return instructions

def processCode(code):
	while not trak[indx] and indx < len(code):
		trak[indx] = True
		run[code[indx][0]](int(code[indx][1]))
	print(accx)
	return not indx < len(code)

def mangleCode(fileName):
	code = processFile(fileName)
	for count, line in enumerate(code):
		global accx, indx, trak
		accx, indx = (0, 0)
		trak = defaultdict(lambda:False)
		if line[0] == 'acc':
			continue
		code[count][0] = 'jmp' if code[count][0] == 'nop' else 'nop'
		if processCode(code):
			print("success at", count)
			break
		code[count][0] = 'jmp' if code[count][0] == 'nop' else 'nop'
	print(accx)

def test1():
	processCode(processFile("day8-t.dat"))

def part1():
	processCode(processFile("day8-1.dat"))

def test2():
	mangleCode("day8-t.dat")

def part2():
	mangleCode("day8-1.dat")

# test1()
# part1()
# test2()
part2()