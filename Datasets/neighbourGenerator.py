import math
import sys
file1 = sys.argv[1]
file2 = sys.argv[3]
maxDist = float(sys.argv[2])
def dist(p1, p2):
	# print(p1,p2)
	p = int(p1[0])-int(p2[0])
	q = int(p1[1])-int(p2[1])
	val = int(math.pow(p,2))+int(math.pow(q,2))
	# val=((p1[0]-p2[0])(p1[0]-p2[0]))+((p1[1]-p2[1])(p1[1]-p2[1]))
	return math.sqrt(val)
list1 = {}
j = 0
with open(file1, 'r') as f:
	for i in f:
		k = i.strip('\n')
		p1 = k.split(',')
		j += 1
		list1[j] = p1
		# print(j)
nbh = {}
for p in range(1, j+1):
	nbh[p] = str(p)
for i in range(1, j+1):
	for m in range(i+1, j+1):
		if(dist(list1[m], list1[i]) <= maxDist):
			nbh[i]+=' '+str(m)
			nbh[m]+=' '+str(i)
with open(file2, 'w') as q:
	for key in nbh:
		q.write(nbh[key])
		q.write('\n')

# print(dist([0,0],[5,4]))
