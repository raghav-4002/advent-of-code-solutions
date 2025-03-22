# Part 1
f = open("1.txt", "r")
string = f.read()

floor = 0

for i in range(0, len(string)):
    if(string[i] == '('):
        floor += 1

    elif (string[i] == ')'):
        floor -= 1

print(floor)

# Part 2
for i in range(0, len(string)):
    if(string[i] == '('):
        floor += 1

    elif(string[i] == ')'):
        floor -= 1

    if(floor == -1):
        break

print(i+1)