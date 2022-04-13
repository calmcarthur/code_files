def checkInt(numPrimes):
    while isinstance(numPrimes, str):
        try:
            numPrimes = int(numPrimes.strip())
            testfor0 = 4/numPrimes

        except:
            numPrimes = input('That is not a valid input, try again: ')
    
    return numPrimes

def TakeInput():

	numPrimes = input("Enter the number of primes you want: ")
	numPrimes = checkInt(numPrimes)

	return numPrimes

def PrintPrimes():

	numPrimes = TakeInput()
	masterNumber = 1
	printCounter = 0

	while printCounter < numPrimes:
		masterNumber += 1
		primeBool = False
		masterDivisor = masterNumber-1
		
		while masterDivisor > 0:
			
			if masterNumber % masterDivisor == 0 and masterDivisor != 1:
				primeBool = True
				break

			masterDivisor -= 1

		if primeBool == False:
			printCounter += 1
			print(masterNumber)
				
if __name__ == "__main__":
	PrintPrimes()
