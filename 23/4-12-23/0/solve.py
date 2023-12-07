file1 = open('input.txt', 'r')
Lines = file1.readlines()

#solution: 25183

sum_total = 0




line_num = 0



for line in Lines:
    line_text = line.strip()
    numbers_on_card = []
    solution_for_line = []
    #print(line_text)
    on_card = line_text.split(":")[1]
    #print(on_card)
    parts = on_card.split("|")
    numbers_on_card = parts[0].split(" ")
    solution_for_line = parts[1].split(" ")
    print(numbers_on_card, solution_for_line)
    matches = 0
    for num in numbers_on_card:
        if num.isnumeric() and num in solution_for_line:
            if matches == 0:
                matches += 1
            else:
                matches = matches * 2

    print("original: ", matches)

    print(matches)

    sum_total += matches




print(sum_total)
