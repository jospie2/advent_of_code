file1 = open('input.txt', 'r')
Lines = file1.readlines()

#solution: 

sum_total = 0




line_num = 0

time_distance = []

for line in Lines:
    line_text = line.strip()
    #print(line_text)
    pos = 0
    
    data = str(line_text.split(":")[1]).split(" ")
        
    for value in data:
        if value.isdigit(): 
            #print(value)
            if line_num == 0:
                time_distance.append([value])
            else:
                time_distance[pos].append(value) 
            pos += 1
    
    line_num += 1

    #sum_total += matches

for vals in time_distance:
    for diff_time in range(vals[0]):

        


print(sum_total)
