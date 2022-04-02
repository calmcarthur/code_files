# file to test stuff

file = open("../../output.txt", 'rt')
list1 = []

for i in file:
    list1.append(i)

print(len(list1))
print(len(set(list1)))