file1 = open('input.txt', 'r')
Lines = file1.readlines()

#solution:

sum_total = 0


location_of_sysmboles_line = []
location_of_sysmboles_pointer = []

location_of_numbers_line = []
location_of_numbers_pointer = []
numbers_with_positions = {}



all_numbers = []

line_num = 0


def next_to(line, posi):
    result = False
    x_check = [-1, 0, 1]
    y_check = [-1, 0, 1]
    line_pos = 0
    position_pos = 0
    for pointer in range(len(location_of_sysmboles_line)):
        for x_value in x_check:
            for y_value in y_check:
                if line + x_value == int(location_of_sysmboles_line[pointer]):
                    if posi + y_value == int(location_of_sysmboles_pointer[pointer]):
                        result = True
                        line_pos = int(location_of_sysmboles_line[pointer])
                        position_pos = int(location_of_sysmboles_pointer[pointer])
    return result, line_pos, position_pos

for line in Lines:
    line_text = line.strip()
    position_pointer = 0
    position_of_last_number_in_line = 0
    numbers_in_line = [""]
    for character in line_text:
        one_number = True
        if not character.isnumeric() and not character == "." and character == "*":
            location_of_sysmboles_line.append(line_num)
            location_of_sysmboles_pointer.append(position_pointer)

        if character.isnumeric():
            #print("number is:", character)
            first = False
            if position_pointer == 0 or len(numbers_in_line[0]) == 0:
                #print("first_number")
                position_of_last_number_in_line = position_pointer
                first = True
                numbers_in_line[0] = str(character)
                location_of_numbers_line.append(line_num)
                location_of_numbers_pointer.append(position_pointer)

            #print(position_of_last_number_in_line, position_pointer - 1)
            if position_of_last_number_in_line == position_pointer - 1:
                position_of_last_number_in_line = position_pointer
                #print("digit next_to digit", numbers_in_line)
                if len(numbers_in_line) == 0:
                    #print("no numbers yet")
                    numbers_in_line[0] = str(character)
                    location_of_numbers_line.append(line_num)
                    location_of_numbers_pointer.append(position_pointer)
                else:
                    #print("there are numbers", len(numbers_in_line))
                    location_of_numbers_line.append(line_num)
                    location_of_numbers_pointer.append(position_pointer)
                    numbers_in_line[len(numbers_in_line)-1] = str(numbers_in_line[len(numbers_in_line)-1]) + str(character)
            elif not first:
                numbers_in_line.append(character)
                position_of_last_number_in_line = position_pointer
                location_of_numbers_line.append(line_num)
                location_of_numbers_pointer.append(position_pointer)
                #print("appendet")
        #print(numbers_in_line)
        #print("last num:", position_of_last_number_in_line)
        #print("")
        position_pointer += 1
    line_num += 1
    all_numbers.append(numbers_in_line)


print("symobl location: ")
print(location_of_sysmboles_line)
print(location_of_sysmboles_pointer)
print("")
print("number location: ")
print(location_of_numbers_line)
print(location_of_numbers_pointer)
print("")
print("numbers")
print(all_numbers)
help_pointer = 0
numbers_next_to_symbol_line = [[],[]]
numbers_next_to_symbol_position = [[],[]]


#80643030
#52910001
#125613183
#75805607
res = []
for num_array in all_numbers:
    last_nums = []
    for numbers in num_array:
        number_colse_to_symbol = False
        if numbers.isnumeric():
            #print("num: ", numbers)

            for number in numbers:
                num_used = []
                #print(help_pointer)
                #print("full number: ", numbers)
                #print("number: ", number)
                #print("location: ")
                #print(location_of_numbers_line[help_pointer], location_of_numbers_pointer[help_pointer])
                #print("is next to symbol: ", next_to(int(location_of_numbers_line[help_pointer]), int(location_of_numbers_pointer[help_pointer])))
                response, line, pos = next_to(int(location_of_numbers_line[help_pointer]), int(location_of_numbers_pointer[help_pointer]))
                if response:
                    #print("response")
                    #print(len(numbers_next_to_symbol_line[1]))
                    #print(numbers)
                    for pointy in range(len(numbers_next_to_symbol_line[1])):
                        if numbers_next_to_symbol_line[1][pointy] == line and numbers_next_to_symbol_position[1][pointy] == pos and not numbers in last_nums and not numbers == numbers_next_to_symbol_line[0][pointy]:
                            print(numbers_next_to_symbol_line[0][pointy], numbers)
                            sum_total += int(numbers_next_to_symbol_line[0][pointy]) * int(numbers)
                            last_nums.append(numbers)
                    numbers_next_to_symbol_line[0].append(numbers)
                    numbers_next_to_symbol_position[0].append(numbers)
                    numbers_next_to_symbol_line[1].append(line)
                    numbers_next_to_symbol_position[1].append(pos)
                    print("")
                help_pointer += 1
print(help_pointer)
print(sum([len(arr) for arr in all_numbers]))
#print(numbers_next_to_symbol_line)
#print(numbers_next_to_symbol_position)

print(sum_total)


"""
for pointer in range(len(numbers_next_to_symbol_line[1])):
if numbers_next_to_symbol_line[1][pointer] == line and numbers_next_to_symbol_position[1][pointer] == pos and not str(numbers) in numbers_next_to_symbol_position[0]:
number_colse_to_symbol = True
print(numbers_next_to_symbol_line[0][pointer], numbers)
print(num_used)
res.append([numbers_next_to_symbol_line[0][pointer], numbers])
num_used.append(numbers)
numbers_next_to_symbol_line[0].append(numbers)
numbers_next_to_symbol_position[0].append(numbers)
numbers_next_to_symbol_line[1].append(line)
numbers_next_to_symbol_position[1].append(pos)
help_pointer += 1
res_test = res
for p in range(len(res)):
sum_total += int(res[p][0]) * int(res[p][1])
"""
