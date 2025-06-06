file = open("input.txt", "r")
strings = file.read()

strings = strings.split("\n")


def condition_3(string):
    for i in range(0, len(string) - 1):
        if (
            string[i : i + 2] == "ab" or
            string[i : i + 2] == "cd" or
            string[i : i + 2] == "pq" or
            string[i : i + 2] == "xy"
            
        ):
            return False

    return True


def condition_2(string):
    for i in range(0, len(string) - 1):
        if string[i] == string[i + 1]:
            return True
    
    return False


def condition_1(string):
    vowels = ["a", "e", "i", "o", "u"]

    vowel_count = 0

    for vowel in vowels:
        vowel_count += string.count(vowel)

    if vowel_count >= 3:
        return True

    return False


def is_nice(string):
    if not condition_3(string):
        return False

    if not condition_2(string):
        return False

    if not condition_1(string):
        return False

    return True


count = 0

for string in strings:
    if is_nice(string):
        count += 1

print(count)