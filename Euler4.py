def getPalidromes(numDigits): #Define the Palidrone Checking Function
	palidromes = []
	for i in range(10 ** numDigits, 10 ** (numDigits + 1) - 1):
		for j in range(10 ** numDigits, 10 ** (numDigits + 1) - 1):
			if str(i * j)== str(i * j)[::-1]:
				palidromes.append(i * j)
	return palidromes

print getPalidromes(3) # Run all of the products through the palindrome checker
