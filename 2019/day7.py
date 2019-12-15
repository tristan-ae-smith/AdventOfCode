from IntCode import IntCode
from itertools import permutations, chain
#test1
# code = "3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0"
# inputs = [4,0,3,0,2,0,1,0,0,0,99,0]

#test2
# code = "3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0"
# inputs = [0,0,1,0,2,0,3,0,4,0,99,0]

#test2
# code = "3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0"
# inputs = [1,0,0,0,4,0,3,0,2,0,99,0]

inpos = 0
attempt = 0
maxSig = 0
 
def locIn(string):
	global inpos
	inpos += 1
	return settings[attempt][inpos-1]

def locOut(out):
	print("putting output",out, "in", inpos+1)
	settings[attempt][inpos+1] = out

settings = permutations(range(5,10))
settings = [list(sum(zip([y for y in x] + [99], [0]*6),())) for x in settings]
print(settings[1])

def part1():
	global maxSig
	with open('day7.dat')	as intInput: # open intCode file
		code = intInput.read()	# read code

		for attempt in range(len(settings)):
			inpos = 0
			A = IntCode(code, locIn, locOut).run(True)
			B = IntCode(code, locIn, locOut).run(True)
			C = IntCode(code, locIn, locOut).run(True)
			D = IntCode(code, locIn, locOut).run(True)
			E = IntCode(code, locIn, locOut).run(True)
			maxSig = max(maxSig, settings[attempt][-1])
		print(maxSig)

def part2():
	global maxSig, inpos
	with open('day7.dat')	as intInput: # open intCode file
		code = intInput.read()	# read code

		for attempt in range(len(settings)):

			inpos = 0
			A = IntCode(code, locIn, locOut)
			B = IntCode(code, locIn, locOut)
			C = IntCode(code, locIn, locOut)
			D = IntCode(code, locIn, locOut)
			E = IntCode(code, locIn, locOut)

			while E.mem[E.pos] != 99:
				inpos = 0
				print(settings[attempt])
				A.run(True)
				return True
				print(settings[attempt])
				B.run(True)
				print(settings[attempt])
				C.run(True)
				print(settings[attempt])
				D.run(True)
				print(settings[attempt])
				E.run(True)
				settings[attempt][1] = settings[attempt][-1] # feedback the final output to the first module
			maxSig = max(maxSig, settings[attempt][-1])
		print(maxSig)

part2()


#todo: this doesn't work because I haven't tested the principles on the exmples because I am an idiot
