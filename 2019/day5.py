from IntCode import IntCode


def test1():
	test1 = {"1,0,0,0,99", "2,3,0,3,99", "2,4,4,5,99,0", "1,1,1,4,99,5,6,0,99"}
	for x in test1:
		y = IntCode(x)
		print(y.run().out())

def testM():
	testM = {"1002,4,3,4,33", "1101,100,-1,4,0"}
	for x in testM:
		y = IntCode(x)
		y.run().writeIntCode()




def locOut(string):
	print(string)

def locIn(string):
	# return input(string)
	return 5

def test2():
	test2 = {"3,9,8,9,10,9,4,9,99,-1,8", "3,9,7,9,10,9,4,9,99,-1,8", "3,3,1108,-1,8,3,4,3,99",
		"3,3,1107,-1,8,3,4,3,99", "3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9", "3,3,1105,-1,9,1101,0,0,12,4,12,99,1",
		"3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99"}
	for x in test2:
		y = IntCode(x, locIn, locOut)
		y.run().writeIntCode()
	
with open('day5.dat')	as intInput: # open intCode file
	code = intInput.read()	# read code
	
	y = IntCode(code, locIn, locOut)
	y.run().writeIntCode()
