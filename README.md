# partialPeriodicSpatialPatterns

Partial Periodic Spatial Pattern Mining (PPSPM) aims to find all neighboring itemsets that occur at regular intervals in a spatiotemporal database. 

The algorithm for PPSPM has been written in Python 3. The command to execute the program is as follows.

python3 partialSpatialPeriodicPatterns.py maxIAT minPS temporalDatabaseFile item_NeighborsFile outputFileName
  
 The maxIAT and minPS values are specified in percentages.
  
 To test the repetability of our experiments, we have provided some databases in the data folder. The details are as follows:
 1. datat10.txt is a synthetic T10I4D100K database used in our experiments. The first column represents the timestamp (or transactional identifier) and remaining columns represents items.
 2. Coordinates.txt file contains the coordinates of the items in datat10.txt file. Please note that the line number implicitly represents the item number in datat10.txt. 
              E.g. the coordinates (x,y) in the first line represent the spatial coordinates for the item whose id is 1 in datat10.txt file.
 3. dist_<Threshold>.txt contains the information regarding the items and their neighbors. The first column in each row represents an item i and remaining columns represents the neighbors of i whose distance is no more than the user-specified <threshold> value.
 4. nbhextracter.py is another python file used to create dist_<threshold>.txt from coordinates.txt file. For brevity,  Euclidean distance is used to compute the distance between the items. The command to execute this file is as follows
      python3 nbhextracter.py <inputCoordinatesFile> <maxDist> <outputFileName>
  
 
 
