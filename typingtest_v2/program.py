from cProfile import run
import time
import random
import linecache

okInput = False

import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
    return None


def getTime():
    global okInput
    print("Welcome to Cal's typing test!")
    time.sleep(1)
    numOfSecs = (input("Enter the length of the test you would like in seconds: ")).strip()

    while okInput == False:

        try:
            numOfSecs = int(numOfSecs)
        
            if (numOfSecs < 1):
                numOfSecs = input("That number is too small, try a number greater than 0: ")
                continue
            if (numOfSecs > 300):
                numOfSecs = input("That number is too large, try a number less than 300: ")
                continue
        except:
            numOfSecs = input("That is not a valid number, try an integer in seconds (ex. 60): ")
            continue

        okInput = True

    return numOfSecs


def runTest():
    numOfSecs = getTime()
    timeEnd = time.time() + numOfSecs

    while time.time() < timeEnd:
        
        # while userInput != currentWord:    
            print(getWord())
            clearConsole()

def getWord():
    randomLine = random.randrange(0, 9100, 1)
    currentWord = linecache.getline("words.txt", randomLine)
    
    return currentWord

runTest()

""" 
ideas for this:

words to type
words ti tyep

top level is words
bottom level is input

if a letter is right it is turned green, if wrong it is turned red, strings are shifted to the left as the user types for the alloted time period

either words per minute and errors is displayed throughout, or at the end, or both
will allow them to delete as far back as they want, will have to figure out how that will affect words per minute (perhaps easier if just calculated at the end in that sense and it doesnt
really affect the user becuase when typing it doesnt matter)

https://stackoverflow.com/questions/24072790/how-to-detect-key-presses

"""

