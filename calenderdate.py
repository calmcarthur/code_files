# unfinished

daybool = False
monthbool = False
yearbool = False
okyear = False
counter = 0
day = 0
month = 0
year = 0
isleapyear = False

while okyear == False:

    counter += 1
    if counter == 1:
        date = input("Please enter a date in the format day/month/year: ")

    listdate = date.split("/")
    print(listdate)

    if len(listdate) != 3:
        date = input("That is not in the format day/month/year, try again: ")
        continue
    try:
        day = int(listdate[0])
        month = int(listdate[1])
        year = int(listdate[2])
        print(day, month, year)
    except:
        date = input("Invalid input, try again in the format day/month/year: ")
        continue

    if (1 > day > 31) or (1 > month > 12) or ((month == 4 or month == 6 or month == 9 or month == 11) and (day > 30))or (year < 1):
        date = input ("Valid input, but that date does not exist, try a new date: ")
        continue
    if month == 2 and day > 29:
        date = input ("Valid input, but that date does not exist, try a new date: ")
        continue        
    if year % 4 == 0:
        isleapyear = True
        if year % 100 == 0 and year % 400 != 0:
            isleapyear = False
    
    if month == 2:
        if isleapyear == True:
            if day > 29:
                date = input("Valid input, but that date does not exist, try a new date: ")
                continue
        elif day > 28:
            date = input("Valid input, but that date does not exist, try a new date: ")
            continue
    
    break

print(day,"/",month,"/",year, "--", isleapyear)