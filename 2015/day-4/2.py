import hashlib

key = "yzbqklnj"
num = 0


def is_zero(sliced_string):
    for i in range(0, 6):
        if sliced_string[i] != "0":
            return False
    
    return True


while True:
    string = key
    
    string += str(num)

    encoded = string.encode()
    hashed_string = hashlib.md5(encoded).hexdigest()
    
    sliced_string = hashed_string[0: 6]

    if(is_zero(sliced_string)):
        break
    
    num += 1

print(num)