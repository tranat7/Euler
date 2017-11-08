import math
def isPrime(i):
	if i < 2:
		return False
	if i == 2:
		return True
	for ii in range(2, i):
		if i % ii == 0:
			return False
	return True

for i in range(100):
	#print str(i) + " - " + str(isPrime(i))
	if isPrime(i):
		primenumber = isPrime(i)

100
50
25
5
1

900
450
225
