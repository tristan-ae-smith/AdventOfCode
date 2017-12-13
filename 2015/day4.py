import hashlib

# check if first 5/6 chars of hash are zero
def fiveZeroes(check):
	# return True if int(check[0:6], 16) == 0 else False	# Part 2
	return True if int(check[0:5], 16) == 0 else False	# Part 1

puzInput = open("day4.dat").read()	# read input seed
print puzInput

mineKey = 1		# start at lowest positive integer without leading zeroes

while not fiveZeroes(hashlib.md5(puzInput+str(mineKey)).hexdigest()):	# while hash not found, continue
	mineKey += 1	# increment before trying again

# print "hash:", hashlib.md5(puzInput+str(mineKey)).hexdigest()
print "key:", mineKey