scores = {}

for it, them in enumerate(['A', 'B', 'C']):
	for iu, us in enumerate(['X', 'Y', 'Z']):
		scores[them+' '+us] = (6 if (3 + iu - it) % 3 == 1 else 0 if (3 + it - iu)%3 == 1 else 3) + iu + 1

print(scores)


def part1(): # find score from guide
	with open('day2-1.dat')	as guideInput:
		items = guideInput.readlines()	# read items
		score = 0
		for item in items:
			score += scores[item.strip()]
		print(score)

part1()


newscores = {}

for it, them in enumerate(['A', 'B', 'C']):
	for iu, us in enumerate(['X', 'Y', 'Z']):
		newscores[them+' '+us] = iu * 3 + ( (2+it)%3 if iu == 0 else (1+it)%3 if iu == 2 else it) + 1

print(newscores)


def part2(): # find score from guide
	with open('day2-1.dat')	as guideInput:
		items = guideInput.readlines()	# read items
		score = 0
		for item in items:
			score += newscores[item.strip()]
		print(score)

part2()