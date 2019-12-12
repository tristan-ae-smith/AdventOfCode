def calculateFuel(mass):
	return max(0, (mass // 3) - 2)

def test1(): # initial examples, visual inspection of output
	test = {12, 14, 1969, 100756}
	print('\n'.join(str(calculateFuel(x)) for x in test))

def part1(): # apply fuel cost calculation to all modules in file and sum
	with open('day1-1.dat')	as massInput: # open module masses file
		masses = massInput.readlines()	# read directions
		masses = [int(mass.strip()) for mass in masses]
		fuelCosts = [calculateFuel(mass) for mass in masses]
		print(sum (fuelCosts), "+")
		return sum(fuelCosts)

def calculateMoreFuel(fuelCost):
	# calculate the additional fuel our initial fuel requires
	moreFuel = calculateFuel(fuelCost)

	#calculate the iteratively smaller amounts to add
	while moreFuel > 0:
		print(moreFuel, "+")
		fuelCost += moreFuel
		moreFuel = calculateFuel(moreFuel)
	return fuelCost

def test2(): # further examples, visual inspection
	test = {12, 14, 1969, 100756}
	fuelCosts = [calculateFuel(mass) for mass in test]
	fuelCosts = [calculateMoreFuel(mass) for mass in fuelCosts]
	print(fuelCosts)

def part2():
	with open('day1-1.dat')	as massInput: # open module masses file
		masses = massInput.readlines()	# read directions
		masses = [int(mass.strip()) for mass in masses]
		fuelCosts = [calculateFuel(mass) for mass in masses]
		fuelCosts = [calculateMoreFuel(mass) for mass in fuelCosts]
		print(sum (fuelCosts), "+")
		return sum(fuelCosts)


part2()