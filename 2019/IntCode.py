class IntCode:
	def __init__(self, codeString, extIn, extOut):
		self.pos = 0
		self.readIntCode(codeString)
		self.opCodes = {
			99: (0, self.ICHalt, 0),
			1: (3, self.ICAdd, 4),
			2: (3, self.ICMult, 4),
			3: (1, self.ICInp, 2),
			4: (1, self.ICOut, 2),
			5: (2, self.ICJit, 0),
			6: (2, self.ICJif, 0),
			7: (3, self.ICClt, 4),
			8: (3, self.ICCeq, 4)
		}
		self.extIn = extIn
		self.extOut = extOut

	def ICHalt(self):
		print("ICHalt should never be called.")
		pass

	def ICAdd(self, modes):
		a = self.mem[self.pos+1] if modes[-1] else self.mem[self.mem[self.pos+1]] # fragile grab of data
		b = self.mem[self.pos+2] if modes[-2] else self.mem[self.mem[self.pos+2]] # fragile grab of data
		self.mem[self.mem[self.pos+3]] = a + b
		self.pos += 4

	def ICMult(self, modes):
		a = self.mem[self.pos+1] if modes[-1] else self.mem[self.mem[self.pos+1]] # fragile grab of data
		b = self.mem[self.pos+2] if modes[-2] else self.mem[self.mem[self.pos+2]] # fragile grab of data
		self.mem[self.mem[self.pos+3]] = a * b
		# print(bool(modes[-1]), modes[-1],modes,a,b,self.mem)
		self.pos += 4

	def ICInp(self, modes): # modes ignored
		inp = self.extIn(("At " + str(self.pos) + " input:"))
		self.mem[self.mem[self.pos+1]] = inp #input
		self.pos += 2

	def ICOut(self, modes): 
		out = self.mem[self.pos+1] if modes[-1] else self.mem[self.mem[self.pos+1]] #output
		self.extOut(("At " + str(self.pos) + " output: " + str(out)))
		self.pos += 2

	def ICJit(self, modes):
		a = self.mem[self.pos+1] if modes[-1] else self.mem[self.mem[self.pos+1]] # fragile grab of data
		b = self.mem[self.pos+2] if modes[-2] else self.mem[self.mem[self.pos+2]] # fragile grab of data
		self.pos = b if a != 0 else (self.pos + 3)
		
	def ICJif(self, modes):
		a = self.mem[self.pos+1] if modes[-1] else self.mem[self.mem[self.pos+1]] # fragile grab of data
		b = self.mem[self.pos+2] if modes[-2] else self.mem[self.mem[self.pos+2]] # fragile grab of data
		self.pos = b if a == 0 else (self.pos + 3)
		
	def ICClt(self, modes):
		a = self.mem[self.pos+1] if modes[-1] else self.mem[self.mem[self.pos+1]] # fragile grab of data
		b = self.mem[self.pos+2] if modes[-2] else self.mem[self.mem[self.pos+2]] # fragile grab of data
		self.mem[self.mem[self.pos+3]] = 1 if a < b else 0
		self.pos += 4

	def ICCeq(self, modes):
		a = self.mem[self.pos+1] if modes[-1] else self.mem[self.mem[self.pos+1]] # fragile grab of data
		b = self.mem[self.pos+2] if modes[-2] else self.mem[self.mem[self.pos+2]] # fragile grab of data
		self.mem[self.mem[self.pos+3]] = 1 if a == b else 0
		self.pos += 4




	def readIntCode(self, string):
		self.mem = [int(x) for x in string.split(",")]
		# print(self.mem)

	def writeIntCode(self):
		print(",".join(map(str,self.mem)))

	def step(self): 
		codestr = str(self.mem[self.pos])
		opcode = int(codestr[-2:])

		if opcode == 99: # early finish
			print("At", self.pos, " halt.")
			return False

		if opcode not in self.opCodes:
			print("An oddity has occured; invalid opcode at ", self.pos)
			return False

		params = self.opCodes[opcode][0] # check how many params this opcode should have
		codestr = ('0'*(params+2 - len(codestr))) + codestr # pad the codestring with 0s for next step

		modes = [True if x == '1' else False for x in codestr[:params]]

		self.opCodes[opcode][1](modes) # call the appropriate operation with list of modes
		# self.pos += self.opCodes[opcode][2] # increment the pointer code-dependently

		return True

	def run(self):
		while self.step():
			pass
		return self

	def out(self):
		return self.mem[0]

	def reset(self, noun, verb):
		self.pos = 0
		self.mem[1] = noun
		self.mem[2] = verb

