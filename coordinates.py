import random

def GenerateCoords():
    lat = str(random.randint(-90,90)) + "."
    long = str(random.randint(-180,180)) + "."

    for i in range(0,6):
        lat = lat + (str(random.randint(0,9)))
        long = long + (str(random.randint(0,9)))

    return lat, long


def PrintCoords():
    lat, long = GenerateCoords()
    print(f"Latitude: {lat} | Longitude: {long}")

    return None


def RunGame():
    counter = 0
    inputGiven = ""

    while (1): # inputGiven != "q":
        # counter += 1

        if counter == 1:
            inputGiven = input("Weclome, press enter to generate a pair of random coordinates: ")
        # else:
        #     inputGiven = input("Press 'enter' to generate another pair of coordinates, or 'q + enter' to exit: ")

        # while inputGiven != "q" and inputGiven != "":
        #     inputGiven = input("Invalid input, press 'enter' to generate a pair of coordinates, or 'q + enter' to exit: ")
        
        if inputGiven == "q":
            continue
        else: 
            PrintCoords()

    return None


# main
if __name__ == '__main__':
	RunGame()	
