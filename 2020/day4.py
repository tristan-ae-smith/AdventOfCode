import re

req = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']
opt = ['cid']

eye = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def byr(value):
	try:
		return True if len(value) == 4 and 1920 <= int(value) <= 2002 else False
	except:
		return False

def iyr(value):
	try:
		return True if len(value) == 4 and 2010 <= int(value) <= 2020 else False
	except:
		return False

def eyr(value):
	try:
		return True if len(value) == 4 and 2020 <= int(value) <= 2030 else False
	except:
		return False

def hgt(value):
	try:
		(num, unit) = re.findall(r"^(\d+)(in|cm)$", value)[0]
		return True if unit == "cm" and 150 <= int(num) <= 193 else \
			   True if unit == "in" and 59 <= int(num) <= 76 else False
	except Exception as inst:
		# print(inst)
		# print(value, "is not a valid height")
		return False

def hcl(value):
	try: 
		# print(value)
		return True if re.match(r"^#[0-9a-f]{6}$", value) else False
	except:
		return False		

def ecl(value):
	try:
		return True if value in eye else False
	except:
		return False

def pid(value):
	try:
		return True if re.match(r"^\d{9}$", value) else False
	except:
		return False

def cid(value):
	return True



checks = {"byr":byr, "iyr": iyr, "eyr":eyr, "hgt":hgt, "hcl":hcl, "ecl":ecl, "pid":pid, "cid":cid,}

def stringToFields(passString):
	fields = re.findall(r"(...):([^ ]+)", passString)
	return fields

def testFieldsToBool(passFields):
	count = 0
	for typ, val in passFields:
		if typ in req:
			count+=1
	print( 'pass' if count >= 7 else 'fail')
	return count >= 7

def testChecksToBool(passFields):
	count = {'ecl': False, 'pid': False, 'eyr': False, 'hcl': False, 'byr': False, 'iyr': False, 'hgt': False }
	for typ, val in passFields:
		if typ in req and checks[typ](val):
			count[typ] = True
	print( 'pass' if sum(count.values()) >= 7 else 'fail')
	return sum(count.values()) >= 7

def fileToLines(filename):
	with open(filename)	as fileInput: # open expense items file
		lines = fileInput.readlines()	# read items
		lines = [line.strip() for line in lines]
		acc = ""
		items = []
		while lines:
			item = lines.pop(0)
			if not item:
				items += [acc]
				acc = ""
				continue
			acc += " " + item
		items += [acc]
		return items

def processFileBasic(fileName):
	lines = fileToLines(fileName)
	valid = 0
	for line in lines:
		print(line)
		fields = stringToFields(line)
		print(fields)
		valid += testFieldsToBool(fields)
	print(valid)

def processFileAdv(fileName):
	lines = fileToLines(fileName)
	valid = 0
	for line in lines:
		# print(line)
		fields = stringToFields(line)
		# print(fields)
		valid += testChecksToBool(fields)
	print(valid)

def test1():
	processFileBasic("day4-t.dat")

def part1():
	processFileBasic("day4-1.dat")

def test2():
	print(byr("2002"))
	print(byr("2003"))
	print(hgt("60in"))
	print(hgt("190cm"))
	print(hgt("190in"))
	print(hgt("190"))
	print(hcl("#123abc"))
	print(hcl("#123abz"))
	print(hcl("123abc"))
	print(ecl("brn"))
	print(ecl("wat"))
	print(pid("000000001"))
	print(pid("0123456789"))
	processFileAdv("day4-t2.dat")

def part2():
	
	processFileAdv("day4-1.dat")

# test1()
# part1()
# test2()
part2()