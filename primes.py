import math

number = 0

while True:
	number += 1
	primebool = False
	divisor = number-1
	
	while divisor > 0:
		
		if number % divisor == 0:
			primebool = True
			break
		
		if divisor <= math.trunc(math.sqrt(number)):
			break

		divisor -= 1

	if primebool == False:
		print(number,"is a prime number")
			

