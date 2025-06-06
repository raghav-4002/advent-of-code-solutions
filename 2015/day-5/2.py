file = open("input.txt", "r")

strings = file.read()
strings = strings.split("\n")


def condition_1(string):
    for i in range(0, len(string) - 2):
        for j in range(i + 2, len(string) - 1):
            if string[i : i + 2] == string[j : j + 2]:
                return True
    
    return False


def condition_2(string):
    for i in range(0, len(string) - 2):
        if string[i] == string[i + 2]:
            return True

    return False


def is_nice(string):
    if not condition_1(string):
        return False

    if not condition_2(string):
        return False

    return True


count = 0
for string in strings:
    if is_nice(string):
        count += 1

print(count)