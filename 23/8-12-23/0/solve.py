
file1 = open('input.txt', 'r')
Lines = file1.readlines()

#solution: 

sum_total = 0






line_num = 0

time_distance = []

comands = []

input_values = []   
input_values_location = []

for line in Lines:
    line_text = line.strip()
    #print(line_text)
    if not line_text == "":
        pos = 0
        if not line_num == 0:
            #print(line_text)
            start = str(line_text.split("=")[0]).replace(" ", "")
            res = str(str(line_text.split("=")[1]).replace("(", "")).replace(")", "")
            left = str(res.split(",")[0]).replace(" ", "")
            right = str(res.split(",")[1]).replace(" ", "")
            #print(start, left, right)
            input_values.append([start, left, right])
            input_values_location.append(start)
        
        data = line_text
    

        for value in data:
            if line_num == 0:
                if value == "R":
                    comands.append(2)
                elif value == "L":
                    comands.append(1)
        
            
    
    line_num += 1

    #sum_total += matches
#print("comands", comands)
#print("vals", input_values)

pointer = 0
check = input_values[0][0]
while True:
    if pointer == len(comands):
        pointer = 0
        #print(pointer)
    #print(comands, pointer)
    #print(input_values[input_values_location.index(check)])
    new_check = input_values[input_values_location.index(check)][comands[pointer]]
    #print(new_check, comands[pointer])
    
    check = new_check
    if check == "ZZZ":
        print("ZZZ")
        break 
    sum_total += 1
    pointer += 1
    

print(sum_total+1)