def part1():
	with open('day3-1.dat')	as sackInput:
		score = 0
		items = sackInput.readlines()
		for item in items:
			halfP = len(item.strip())//2
			half = item[halfP:]
			for letter in item[:halfP]:
				if letter in half:
					score += ord(letter) - 38 if letter.isupper() else ord(letter) -96
					break
		print(score)

# part1()

def part2():
	with open('day3-1.dat')	as sackInput:
		score = 0
		items = sackInput.readlines()
		it = iter(items)
		for elfA, elfB, elfC in zip(it, it, it):
			for badge in elfA:
				if badge in elfB and badge in elfC:
					score += ord(badge) - 38 if badge.isupper() else ord(badge) -96
					break
		print(score)

part2()
