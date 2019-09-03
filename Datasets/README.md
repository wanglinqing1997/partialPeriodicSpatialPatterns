# Details of the datasets


|Dataset| Format|
|-------|-------|
|T10I4D100K.txt|  timestamp/rowID item 1, item 2, .....|
|coordinates.txt| x-coordinates,y-coordinates|
|dist_threshold.txt|item neighboringItems|


# COMMAND to execute
> python3 neighbourGenerator.py coordinatesInputFile.txt *distanceThreshold* outputItemNeighborsFile.txt

# Example 
>python3 neighbourGenerator.py coordinates.txt 10 dist_10.txt
