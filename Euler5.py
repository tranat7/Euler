import itertools

def isDivisible(num, min, max):
	for n in range(min, max):
		if num % n != 0:
			return False
	return True

for num in itertools.count(1):
	if isDivisible(num, 1, 20):
		print num
		break


