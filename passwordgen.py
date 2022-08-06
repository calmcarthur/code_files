import random
import string

length = 'not a number'

def checkInt():
    global length
    while isinstance(length, str):
        try:
            length = int(length.strip())
            checkLength()
        except:
            length = input('That is not a valid input, try again: ')
            continue

def checkLength():
    global length
    while length not in range(1,51):
        length = int(input('That is not a valid length, try a number between 0 and 50: '))

def getNumber(length):

    dividers = random.sample(range(1,length),2)
    dividers.sort()

    randList = [dividers[0] - 0, dividers[1] - dividers[0], length - dividers[1]]

    for i in range(3):
        randListChoice = random.choice(randList)
        if i == 0:
            numUpperCase = randListChoice
        if i == 1:
            numLowerCase = randListChoice
        if i == 2:
            numNumbers = randListChoice
        randList.remove(randListChoice)
    
    return numUpperCase, numLowerCase, numNumbers
    
def genPassword(numUpperCase, numLowerCase, numNumbers):
    passwordList = []
    password = ''
    for i in range(numUpperCase):
        tempChar = random.choice(string.ascii_uppercase)
        passwordList.append(tempChar)

    for i in range(numLowerCase):
        tempChar = random.choice(string.ascii_lowercase)
        passwordList.append(tempChar)

    for i in range(numNumbers):
        tempChar = str(random.randint(0,9))
        passwordList.append(tempChar)

    random.shuffle(passwordList)

    for i in passwordList:
        password = password + i

    return password 

def runProgram():
    global length
    programOn = True
    counter = 0
    while (programOn == True):
        counter += 1
        if counter == 1:
            print('Hello, welcome to Cal\'s secure password generator')
            length = input('First, put in the desired length of your password: ')

            checkInt()
            numUpperCase, numLowerCase, numNumbers = getNumber(length)
            password = genPassword(numUpperCase, numLowerCase, numNumbers)
            print("\033[32mHere is your password:\033[0m\n", password)
        else:
            print("\033[34m-----------------------------------------------------\033[0m")
            length = input('Type a length to get another password or \'q\' to exit: ')
            if length == 'q':
                programOn = False
            else:
                checkInt()
                numUpperCase, numLowerCase, numNumbers = getNumber(length)
                password = genPassword(numUpperCase, numLowerCase, numNumbers)
                print("\033[32mHere is your password:\033[0m\n", password)

    return None      

# main
runProgram()