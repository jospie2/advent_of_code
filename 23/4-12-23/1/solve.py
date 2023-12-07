file1 = open('input.txt', 'r')
Lines = file1.readlines()

#solution: 5667240

sum_total = 0
copie_of_card = {}
cards = []
num_of_cards = 0

for line in Lines:
    num_of_cards += 1
    line_text = line.strip()
    numbers_on_card = []
    solution_for_line = []
    #print(line_text)
    on_card = line_text.split(":")
    card_num = int(on_card[0].replace("Card", ""))
    parts = on_card[1].split("|")
    numbers_on_card = parts[0].split(" ")
    solution_for_line = parts[1].split(" ")
    #print(numbers_on_card, solution_for_line)
    matches = 0
    for num in numbers_on_card:
        if num.isnumeric() and num in solution_for_line:
            matches += 1

    if matches >= 0:
        copie_of_card.update({card_num:{"matches": matches}})
        cards.append(card_num)
        #print("original: ", matches)

    #print(matches)
#print(matches)


cards_to_multiply_by = {}
sum_total += num_of_cards
while True:
    #print("cards:", cards)
    if len(cards) == 0:
        break
    new_cards = []
    for values in cards:
        #print(values, copie_of_card[values]["matches"])

        for card in range(copie_of_card[values]["matches"]+1):
            if not card == 0:
                #print(values+card)
                new_cards.append(values+card)
                #print(new_cards)
                sum_total += 1
    cards = new_cards



#print(copie_of_card)
#print(new_cards)
print(sum_total)
