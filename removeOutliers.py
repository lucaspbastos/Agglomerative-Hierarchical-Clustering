import sys
import ast
import math

def distance(p1, p2):
    # Returns distance between two points
    return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2 + (p2[2]-p1[2])**2)

# S dataset file, p (fraction), and d (distance) as input for DB(p, d)
pointFile = sys.argv[1]
p = float(sys.argv[2])
D = int(sys.argv[3])
totalPoints = []
toRemove = []

if p < 0 or p > 1:
    print("Error: fraction must be between 0 and 1")
    exit()

# Assign points from S to array
f = open(pointFile, "r")
for line in f:
    point = ast.literal_eval(line.strip())
    totalPoints.append(point)
f.close()

# Set number of points to the fraction of total points 
thresh = int(round((p) * (len(totalPoints)-1)))

for i in range(len(totalPoints)):
    count = 0
    # Check if distance is within D for each other point
    for q in totalPoints:
        if totalPoints[i] != q:
            d = distance(totalPoints[i], q)
            # If distance is greater than D, increase count
            if d > D:
                count += 1
    # If count is greater than thresh
    if count > thresh:
        toRemove.append(i)

print("Removing {} outliers from S where points have at least {} points ({}%) further than {} distance, into S' dataset file {}".format(len(toRemove), thresh, p*100, D, pointFile.split(".")[0]+"-OR."+pointFile.split(".")[1]))

# Sort toRemove in ascending order to iterate for removal from S to become S'
toRemove.sort(reverse=True)
for i in toRemove:
    print("Removing point {}".format(totalPoints[i]))
    del totalPoints[i]

# Write new S' dataset file
f = open(pointFile.split(".")[0]+"-OR."+pointFile.split(".")[1], "w")
for point in totalPoints:
    f.write(str(point) + "\n")
f.close()