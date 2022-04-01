x = int(input('\nWelcome to the Collatz Conjecture Script. This script takes any positive integer and computes it to 1. How? \nWell,\
 if a number is odd, it is multiplied by 3 and 1 is added. If a number is even, it is divided by two.\
 This process is repeated until the given number reaches 1.\
 All numbers supposedly reach this "Four Loop" where the number ends at 1... though this has yet to be proven by even the\
 smartest mathematicians in the world.\nEnter any number to see this in action:'))

counter = int(0)

while x != 1:
    if x % 2 == 0:
        
        x = x/2
        
        print(x)

        counter = counter + 1

    else:

        x = (x*3)+1

        print(x)

        counter = counter + 1

print('Steps to Completion:' , counter)
print('And there you see, any number will end at 1... though we do not know this for sure!')