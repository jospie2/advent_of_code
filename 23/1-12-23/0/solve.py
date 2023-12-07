file1 = open('input.txt', 'r')
Lines = file1.readlines()

#solution: 54708

total_sum = 0
charaters_allowed = ["0","1","2","3","4","5","6","7","8","9"]

for line in Lines:
    nums_in_line = []
    for charac in line.strip():
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
