file1 = open('input.txt', 'r')
Lines = file1.readlines()

#solution: 2727

sum_total = 0
coulours = ["red", "green", "blue"]
num_of_cubes_allowed = {"red": 12, "blue": 14, "green": 13}

for line in Lines:
    roll_valid = True
    line_text = line.strip()
    print("line: ", line_text)
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
                    if not amount <= num_of_cubes_allowed[check_coulour.replace(" ", "")]:
                        #print("id: ", game_id)
                        #print(amount, check_coulour)
                        roll_valid = False
                

    #print(game_id, roll_valid)
    #print("")
    if roll_valid:
        sum_total += game_id



print(sum_total)
