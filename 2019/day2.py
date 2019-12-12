class IntCode:
	def __init__(self, codeString):
		self.pos = 0
		self.readIntCode(codeString)

	def readIntCode(self, string):
		self.mem = [int(x) for x in string.split(",")]
		# print(self.mem)

	def writeIntCode(self):
		print(",".join(map(str,self.mem)))

	def step(self):
		opcode = self.mem[self.pos]
		if opcode == 99: # early finish
			return False
		elif opcode == 1: # add two ints a & b and store in out
			a = self.mem[self.mem[self.pos+1]] # fragile grab of data
			b = self.mem[self.mem[self.pos+2]] # fragile grab of data
			self.mem[self.mem[self.pos+3]] = a + b
			self.pos += 4
			return True
		elif opcode == 2: # add two ints a & b and store in out
			a = self.mem[self.mem[self.pos+1]] # fragile grab of data
			b = self.mem[self.mem[self.pos+2]] # fragile grab of data
			self.mem[self.mem[self.pos+3]] = a * b
			self.pos += 4
			return True
		else:
			print("An oddity has occured; invalid opcode at ", self.pos)
			return False

	def run(self):
		while self.step():
			pass

	def out(self):
		return self.mem[0]

	def reset(self, noun, verb):
		self.pos = 0
		self.mem[1] = noun
		self.mem[2] = verb


from itertools import product

def test1():
	test1 = {"1,0,0,0,99", "2,3,0,3,99", "2,4,4,5,99,0", "1,1,1,4,99,5,6,0,99"}
	for x in test1:
		y = IntCode(x)
		y.run()

with open('day2-1.dat')	as intInput: # open intCode file
	code = intInput.read()	# read code

	for x,y in product(range(100),repeat=2):
		print(x, y)
		program = IntCode(code)
		program.reset(x,y)
		program.run()
		if program.out() == 19690720:
			print(x, y)
			break
