def getMaxPalidrome(min, max): #Define the Palidrone Checking Function
	_max = 0
	for i in range(min, max):
		for j in range(min, max):
			if str(i * j)== str(i * j)[::-1] and i * j > _max:
				_max = i * j
	return _max

print getMaxPalidrome(100, 999) # Run all of the products through the palindrome checker
