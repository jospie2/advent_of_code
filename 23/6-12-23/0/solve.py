import numpy as numpy
file1 = open('input.txt', 'r')
Lines = file1.readlines()

#solution: 449820

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
                time_distance.append([int(value)])
            else:
                time_distance[pos].append(int(value)) 
            pos += 1
    
    line_num += 1

    #sum_total += matches
times = []
for vals in time_distance:
    #print(vals[0])
    best_time = []
    for diff_time in range(vals[0]):
        if diff_time*(vals[0] - diff_time) > vals[1]:
            best_time.append([diff_time*(vals[0] - diff_time), diff_time])

    times.append(len(best_time))
        


print(sum_total)
print(numpy.prod(times))