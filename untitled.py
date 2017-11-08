def isPrime(i):
	for ii in range(2, i - 1):
		if i % ii == 0:
			return False
		else:
			return True

for i in range(100):
	print i + " - " + isPrime(i)