import time

# Run this program to print out all the ascii character codes and what they do into terminal.

def createList():

    list = []

    for i in range(0,5):
        list.append(i)

    for i in range(7,10):
        list.append(i)

    list.append(21)

    for i in range(30,37):
        list.append(i)

    for i in range(41,48):
        list.append(i)

    for i in range(90,97):
        list.append(i)

    for i in range(100,108):
        list.append(i)

    return list

def printStartMsg():

    print("Hello, this program prints out all the ascii terminal character codes, there are 37 total.")
    time.sleep(3)
    print("Use the following code format '\\033[0m TextHere \\033[0m' where the first 0 is replaced with your ascii code")
    time.sleep(4)
    input("\nPress enter to print the list: ")
    print()

    return None

def printStrings():

    startString = "This is what ascii code number "
    startSeq = "\033["
    middleSeq = "m"
    endString = " does!"
    endSeq = "\033[0m"
    counter = -1
    
    list = createList()

    for codeCounter in list:

        counter += 1
        codeCounterStr = str(codeCounter)

        if counter == 0:
            printString = "The 0 character code is the escape. It is used at the end of your string to revert ascii changes."
        else:
            printString = startSeq + codeCounterStr + middleSeq + startString + codeCounterStr + endString + endSeq
        
        if codeCounter < 10:
            print(codeCounterStr, "  |", printString)

        if codeCounter > 9 and codeCounter < 100:
            print(codeCounterStr, " |", printString)
        
        if codeCounter > 99:
            print(codeCounterStr, "|", printString)
        
        time.sleep(0.1)

    return None

# main
printStartMsg()
printStrings()