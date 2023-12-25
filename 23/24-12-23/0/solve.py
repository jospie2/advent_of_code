file1 = open('input.txt', 'r')
Lines = file1.readlines()

#solution: 

sum_total = 0




line_num = 0



for line in Lines:
    line_text = line.strip()
    
    parts = line_text.split("@")
    start_cords = parts[0].split(",")[:-1]
    velocities = parts[1].split(",")[:-1]
    print(start_cords)
    print(velocities)
    
    for cords in zip(start_cords, velocities):
        print(cords)




print(sum_total)
