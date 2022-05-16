import sys
import ast
import math

def distance(p1, p2):
    # Returns distance between two points
    return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2 + (p2[2]-p1[2])**2)

def clusterDistance(c1, c2, type):
    # Returns distance between two clusters
    # Types: 1 = min, 2 = max, 3 = avg, 4 = center
    if type == 4:
        # Initial point of cluster center
        centerp1 = (0, 0, 0)
        centerp2 = (0, 0, 0)

        # Find center of clusters by averaging points
        for p in c1:
            centerp1 = (centerp1[0] + p[0], centerp1[1] + p[1], centerp1[2] + p[2])
        for p in c2:
            centerp2 = (centerp2[0] + p[0], centerp2[1] + p[1], centerp2[2] + p[2])
        centerp1 = (centerp1[0]/len(c1), centerp1[1]/len(c1), centerp1[2]/len(c1))
        centerp2 = (centerp2[0]/len(c2), centerp2[1]/len(c2), centerp2[2]/len(c2))

        # Find distance between centers
        dis = distance(centerp1, centerp2)
    else:
        if type == 1:
            # For min distance, start at high number
            dis = math.inf
        else:
            # For max and avg distance, start at low number
            dis = 0
        for p in c1:
            for q in c2:
                d = distance(p, q)
                if type == 1:
                    # For min distance, compare to current min
                    if d < dis:
                        dis = d
                elif type == 2:
                    # For max distance, compare to current max
                    if d > dis:
                        dis = d
                else:
                    # For avg distance, add to current distance
                    dis += d
        if type == 3:
            # For avg distance, divide by number of points in both clusters
            dis /= (len(c1) + len(c2))
    return dis

# S' dataset file, kclusters, and distance type as input
Sprime = sys.argv[1]
kcluster = int(sys.argv[2])
distanceType = int(sys.argv[3])
totalPoints = []
clusters = []
silhoutteCoefficients = []
typeTable = {1: "min", 2: "max", 3: "avg", 4: "center"}

if kcluster < 0:
    print("Error: k must be greater than 0")
    exit()
if distanceType > 4 or distanceType < 1:
    print("Error: type must be 1, 2, 3, or 4")
    exit()

# Read S' dataset file to assign points to own clusters
f = open(Sprime, "r")
for line in f:
    point = ast.literal_eval(line.strip())
    totalPoints.append(point)
    clusters.append([point])
f.close()

if kcluster > len(totalPoints):
    print("Error: k must be less than or equal to the number of points")
    exit()

# Begin clustering until k clusters reached
clusterSize = len(clusters)
while (clusterSize > kcluster):
    # Find closest clusters on each round of merging
    smallest_distance = math.inf
    for i in range(clusterSize):
        for n in range(clusterSize):
            if i != n:
                d = clusterDistance(clusters[i], clusters[n], distanceType)
                if d < smallest_distance:
                    # Get smallest distance between 2 clusters, save cluster indexes
                    smallest_distance = d
                    smallest1 = i
                    smallest2 = n
    # Merge closest clusters
    for each in clusters[smallest2]:
        clusters[smallest1].append(each)

    # Remove leftover cluster
    del clusters[smallest2]
    clusterSize = len(clusters)

# Calculate Silhouette Coefficient
for p in totalPoints:
    avgDistances = []
    a = 0
    # Find distance between chosen point and all other points in clusters
    for c in clusters:
        totalDistance = 0
        for q in c:
            if p != q:
                totalDistance += distance(p, q)
        avgDistance = totalDistance / len(c)

        # If chosen point in own cluster, set to a
        if p in c:
            a = avgDistance
        else:
            avgDistances.append(avgDistance)
    if (len(avgDistances) == 0):
        # If no other clusters, set to 0
        b = 0
    else:
        b = min(avgDistances)
    # Calculate Silhouette Coefficient
    s = (b - a) / max(a, b)
    silhoutteCoefficients.append(s)

print("Average Silhouette Coefficient: {} for {} clusters (with {} points) with {} cluster distance".format(sum(silhoutteCoefficients) / len(silhoutteCoefficients), kcluster, len(totalPoints), typeTable[distanceType]))