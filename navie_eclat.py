#!/usr/bin/env python
# coding: utf-8

# In[8]:

import sys
FreqItems = dict()
per=float(sys.argv[1])
per_freq=float(sys.argv[2])
final_data=dict()
nbh_dict=dict()


def eclat(prefix, items,nbh_prefix):
    while items:
        i,itids = items.pop()
        if j in nbh_prefix:
            yield (prefix + [i])
            nbh_sent=nbh_prefix & nbh_dict[i]
			# print(prefix + [i])
            suffix = []
            for j, ojtids in items:
        	   	jtids = itids & ojtids
        		if verify(jtids) == 0:
        			suffix.append((j,jtids))
        # print(suffix)
            for pat in eclat(prefix+[i], sorted(suffix, key=lambda item: len(item[1]), reverse=False),nbh_sent):
        	   yield pat




def Read_Data(filename):
    data = {}
    trans = 0
    f = open(filename, 'r')
    for row in f:
        k=row.split()
        for item in k[1:]:
            if item not in data:
                data[item] = set()
            data[item].add(int(k[0]))
    f.close()
    final_data={ k: v for k, v in data.items() if  verify(v)==0}
    return final_data


# In[13]:


def verify(tids):
    tids = list(tids)
    tids.sort()
    if(len(tids)>0):
    	cur = tids[0]
    pf = 0
    for j in range(1, len(tids)):
        if (tids[j] - cur <= per):
            pf += 1
        cur = tids[j]
    if pf>=per_freq:
        return 0
    else:
        return 1


# In[11]


if __name__ == "__main__":
    dict_id = 0
    data = Read_Data(sys.argv[3]) #change the delimiter based on your input file
    with open(sys.argv[4],'r') as nbh:
        for line in nbh:
        	li=line.split()
        	if li[0] in data:
        		ds=set()
        		for i in range(1,len(li)):
        			if li[i] in data:
        				ds.add(li[i])
        		nbh_dict[li[0]]=ds
                
    nbh.close()
    init_nbh=set()
    for j in nbh_dict:
    	init_nbh.add(j)
    print('finished reading data..... \n Starting mining .....')
    k=eclat([], sorted(data.items(), key=lambda item: len(item[1]), reverse=False),init_nbh )
    # print('found %d Frequent items' % len(FreqItems))
    with open(sys.argv[5], 'w') as f:
        for x in k:
            f.write('%s \n'%str(x))
