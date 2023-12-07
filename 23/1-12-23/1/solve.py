file1 = open('input.txt', 'r')
Lines = file1.readlines()

# solution: 54087

total_sum = 0
charaters_allowed = ["0","1","2","3","4","5","6","7","8","9"]
number_in_charaters_allowed = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
number_in_charaters_translated = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
nums_in_line = []

for line in Lines:
    nums_in_line = []
    line_text = line.strip()
    
    for val in number_in_charaters_translated:
        line_text = line_text.replace(val, val+number_in_charaters_translated[val]+val)

    for charac in line_text:
        if charac in charaters_allowed:
            nums_in_line.append(charac)
    
    length = len(nums_in_line)
    sum = []
    sum_str = ""

    if length == 1:
        sum.append(nums_in_line[0])
        sum.append(nums_in_line[0])
    elif length == 2:
        sum.append(nums_in_line[0])
        sum.append(nums_in_line[1])
    elif length > 2:
        sum.append(nums_in_line[0])
        sum.append(nums_in_line[-1])
    sum_str = ''.join(sum)
    total_sum += int(sum_str)
    
print(total_sum)

