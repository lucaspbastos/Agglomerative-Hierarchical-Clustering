import random
import sys

# Create a file for S dataset with name and number of points as input 
f = open(sys.argv[1]+".txt", "w")
num = int(sys.argv[2])
points = []

# Generate S dataset of 3 dimensional points into file
for i in range(num):
    point = (random.uniform(0, 10), random.uniform(0, 10), random.uniform(0, 10))
    f.write(str(point) + "\n")
f.close()

print("S dataset file {} created with {} points".format(sys.argv[1]+".txt", num))