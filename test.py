# file to test stuff

numPrimes = 'hello'

def TryStuff():
    while isinstance(numPrimes, str):
        try:
            numPrimes = int(numPrimes.strip())
            testfor0 = 4/numPrimes

        except:
            numPrimes = input('That is not a valid input, try again: ')
    
    return None