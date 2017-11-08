#collatz script
def collatz(userNumber) : 

 if userNumber % 2 == 0:
          print(userNumber // 2)
          return userNumber // 2

 elif userNumber % 2 == 1:
        result = 3 * userNumber + 1
        print(result)
        return result
n = input('Pick a number')
try:
 while n != 1:
    n = collatz(int(n))
except:
    print('This is not a number')
