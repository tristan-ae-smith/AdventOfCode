

def testNum1(num):
	same = False
	num = str(num)
	prev = num[0]
	for d in num[1:]:
		if prev == d: same = True
		if d < prev: return False
		prev = d
	return same

def testNum2(num):
	num = str(num)
	comp = [[num[0], 1]]
	for d in num[1:]:
		# print(comp, d)

		if d < comp[-1][0]: return False
		elif d == comp[-1][0]: comp[-1][1] += 1
		else: comp += [[d, 1]]
	# print(comp)
	for pair in comp:
		if pair[1] == 2:
			return True
	return False

print(testNum1(111111)) #true
print(testNum1(223450)) #false
print(testNum1(123789)) #false
print(testNum1(455544)) #false

print(testNum2(111111)) #false
print(testNum2(223450)) #false
print(testNum2(123789)) #false
print(testNum2(455544)) #false
print(testNum2(112233)) #true
print(testNum2(123444)) #false
print(testNum2(111122)) #true

sumP = 0
for passcode in range(248345, 746315):
	# print (passcode, testNum(passcode))
	sumP += int(testNum2(passcode))
print(sumP)