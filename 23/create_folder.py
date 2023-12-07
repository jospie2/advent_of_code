import os



for num in range(24):
    for num_dir in range(2):
        dirName = str(num) + "-12-23/" + str(num_dir)
        os.makedirs(dirName)
	      