
def SumOfSquares(min, max):
	thesum = 0
	for num in range(min, max):
		thesum += num ** 2
	return thesum


def SquareOfSums(min, max):
	sumnum = 0
	for i in range(min, max):
		sumnum += i
	return sumnum ** 2

answer = SquareOfSums(1,101) - SumOfSquares(1, 101) 
print answer
