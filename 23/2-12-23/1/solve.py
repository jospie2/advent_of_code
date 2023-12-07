file1 = open('input.txt', 'r')
Lines = file1.readlines()

#solution: 56580

sum_total = 0
coulours = ["red", "green", "blue"]


for line in Lines:
    smalest_num_of_colour_in_set = [0,0,0]
    line_text = line.strip()
    game_id = int(str(line_text.split(":")[0]).replace("Game", ""))
    rolls = line_text.split(":")
    rolls = str(rolls[1])
    rolls = rolls.split(";")
    for roll in range(len(rolls)):
        colours_revealed = rolls[roll].split(",")
        #print(colours_revealed)
        for reveales in colours_revealed:
            for check_coulour in coulours:
                if check_coulour in reveales:
                    amount = int(reveales.replace(check_coulour, ""))
                    print(check_coulour, amount)

                    if check_coulour == "red":
                        if amount > smalest_num_of_colour_in_set[0]:
                            smalest_num_of_colour_in_set[0] = amount
                    if check_coulour == "green":
                        if amount > smalest_num_of_colour_in_set[1]:
                            smalest_num_of_colour_in_set[1] = amount
                    if check_coulour == "blue":
                        if amount > smalest_num_of_colour_in_set[2]:
                            smalest_num_of_colour_in_set[2] = amount
                

    print(game_id, smalest_num_of_colour_in_set)
    print("")
    sum_of_roll = smalest_num_of_colour_in_set[0] * smalest_num_of_colour_in_set[1] * smalest_num_of_colour_in_set[2]
    sum_total += sum_of_roll



print(sum_total)
