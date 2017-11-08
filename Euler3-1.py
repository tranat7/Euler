import itertools

def largestPrime(s):
	_max = -1;
	for i in itertools.count(2):
		while s % i == 0:
			s /= i
			_max = i
		if s == 1:
			break
	return _max
	

print largestPrime(600851475143)



"""
100
50
25
5
1
"""