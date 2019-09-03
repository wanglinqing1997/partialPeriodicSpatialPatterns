#Details of the datasets


|Dataset| Format|
|-------|-------|
|T10I4D100K.txt|  timestamp/rowID item 1, item 2, .....|
|coordinates.txt| x-coordinates,y-coordinates|
|T10I4D100K.txt|item neighbors with **distanceThreshold** of 10|


#command to generate neighbours for items
> python3 neighbourGenerator.py coordinates.txt **distanceThreshold** dist_threshold.txt
