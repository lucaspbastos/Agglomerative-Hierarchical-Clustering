# Agglomerative Hierarchical Clustering Program
Course: C634 - Data Mining at New Jersey Insitute of Technology

Instructor: Professor Haodi Jiang

## Generate Points
Generates a dataset text file with specified number of 3 dimensional points between 0 and 10 in all dimensions.

Usage: `python3 generatePoints.py [output dataset file name] [number of points]`

Example: `python3 generatePoints.py set.txt 500`

## Remove Outliers
Removes the outliers from a dataset text file and places into a new dataset text file with a distance based algorithm that finds and removes a specified fraction p of the points in the dataset that lie at a specified distance greater than D.

Usage: `python3 removeOutliers.py [input dataset file name] [0 < p fraction of points < 1] [distance threshold D > 0]

Example: `python3 removeOutliers.py set.txt 0.7 7`

## Agglomerative Hierarchical Clustering
Clusters the points into a specified k-cluster count and a specified clustering distance measuring type.

Usage: `python3 clusteringProj.py [input dataset file name] [k cluster count > 0] [cluster distance measuring type 0-4]

Where cluster distance measuring types are: 1=min, 2=max, 3=avg, 4=center. Using the center measuring type typically yields the best Silhouette Coefficient.

Example: `python3 clusteringProj.py set-OR.txt 150 4`