# Part 1

test_file = open("input.txt", "r")
string = test_file.read()

dimension_list = string.split('\n')

for i in range(0, len(dimension_list)):
    dimension_list[i] = dimension_list[i].split('x')

for parameters in dimension_list:
    for j in range(0, len(parameters)):
        parameters[j] = int(parameters[j])

total_area = 0
total_ribbon_length = 0

for box in dimension_list:
    l = box[0]
    w = box[1]
    h = box[2]

    min_area = min([l*w, w*h, h*l])
    min_perimeter = min([2*(l + w), 2*(w + h), 2*(h + l)])

    volume = l * w * h

    total_ribbon_length += volume + (min_perimeter)

    total_area += min_area + (2*l*w + 2*w*h + 2*h*l)


print(total_area)    
print(total_ribbon_length)