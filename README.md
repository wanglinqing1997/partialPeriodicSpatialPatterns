# partialPeriodicSpatialPatterns

Partial Periodic Spatial Pattern Mining (PPSPM) aims to find all neighboring itemsets that occur at regular intervals in a spatiotemporal database. 

The algorithms, n_ECLAT and ST_ECLAT, have  been written in Python 3. The command to execute the program is as follows.

> python3 ST_ECLAT.py *maxIAT* *minPS* **temporalDatabaseFile item_NeighborsFile outputFileName**

> python3 n_ECLAT.py *maxIAT* *minPS* **temporalDatabaseFile item_NeighborsFile outputFileName**
  
 The *maxIAT* and *minPS* values are specified in percentages.
  
 To test the repetability of our experiments, we have provided some databases in the **Datasets** folder. The details are as follows:
 1. **data_t10.txt** is a synthetic T10I4D100K database used in our experiments. The first column represents the timestamp (or transactional identifier) and remaining columns represents items.
 2. **Coordinates.txt** file contains the coordinates of the items in datat10.txt file. Please note that the line number implicitly represents the item number in datat10.txt. 
           E.g. the coordinates (x,y) in the first line represent the spatial coordinates for the item whose id is 1 in datat10.txt file.
 3. **dist_Threshold.txt** contains the information regarding the items and their neighbors. The first column in each row represents an item i and remaining columns represents the neighbors of i whose distance is no more than the user-specified threshold value.
 4. **nbhextracter.py** is another python file used to create dist_Threshold.txt from coordinates.txt file. For brevity,  Euclidean distance is used to compute the distance between the items. The command to execute this file is as follows
      > python3 nbhextracter.py **inputCoordinatesFile** *maxDist* **outputFileName**
      
      
      
## Examples of running above code
>python3 partialSpatialPeriodicPatterns.py *1* *0.1* **./Datasets/data_t10.txt ./Datasets/dist_10.txt patterns_dist_10.txt**

> time -v python3 partialSpatialPeriodicPatterns.py *1* *0.1* **./Datasets/data_t10.txt ./Datasets/dist_10.txt patterns_dist_10.txt** (ubuntu)

>/opt/local/libexec/gnubin/time -v python3 partialSpatialPeriodicPatterns.py *1* *0.1* **./Datasets/data_t10.txt ./Datasets/dist_10.txt patterns_dist_10.txt** (Mac)
  
 
 
