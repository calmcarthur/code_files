import time
from random import sample
import linecache
import os
import keyboard

def CheckTerminalSize():
    columns, lines = os.get_terminal_size()

    if columns < 80 or lines < 5:
        print("Please make your terminal larger.")

        while columns < 80 or lines < 5:
            columns, lines = os.get_terminal_size()
            time.sleep(1)
    
    ClearConsole()


def ClearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
    
    return None


def WaitToStart(firstLetter):
    
    print(firstLetter)

    while(True):
        if keyboard.is_pressed(firstLetter):
            break


def TestSetup():

    okInput = False
    print("Welcome to Cal's typing test!")
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
    
    time.sleep(0.3)
    ClearConsole()
    masterWordList = GetWordList(numOfSecs)
    WaitToStart(masterWordList[0][0])

    return numOfSecs, masterWordList


def GetWordList(numOfSecs):
    
    wordList = sample(range(1, 9100), numOfSecs*4)

    for i in range(1, (numOfSecs*4)+1):
        
        wordList[i-1] = linecache.getline("words.txt", wordList[i-1]).strip()

    return wordList


def TypingMain():
    numOfSecs, masterWordList = TestSetup()
    timeEnd = time.time() + numOfSecs

    counter = 0

    while time.time() < timeEnd:
        counter += 1
        time.sleep(1)
        print(masterWordList[counter])
   
    return None


def RunTest():
    CheckTerminalSize()
    TypingMain()

    return None


if __name__ == "__main__":
    RunTest()


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

