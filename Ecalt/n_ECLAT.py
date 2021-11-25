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
        i, itids = items.pop()
        isupp = len(itids)
        if i in nbh_prefix:
            yield(prefix + [i])
            nbh_sent = nbh_prefix & nbh_dict[i]
            suffix = []
            for j, ojtids in items:
                jtids = itids[0] & ojtids[0]
                pf_alpha=verify(jtids)
                if pf_alpha>= per_freq:
                    suffix.append((j,[jtids,pf_alpha]))
            for pat in eclat(prefix+[i], sorted(suffix, key=lambda item: item[1][1], reverse=False), nbh_sent):
                yield pat

def Read_Data(filename):
    vertical_data = {}
    trans = 0
    f = open(filename, 'r')
    for row in f:
        k=row.split()
        for item in k[1:]:
            if item not in vertical_data:
                vertical_data[item] = set()
            vertical_data[item].add(int(k[0]))
    f.close()
    vertical_dataPF={}
    for k in vertical_data:
        perf_k = verify(vertical_data[k])
        if perf_k>=per_freq:
            vertical_dataPF[k]=[vertical_data[k],perf_k]
    # print(vertical_dataPF['127'])
    # final_data={ k: v for k, (v,verify(v)) in data.items() if  verify(v)==0}
    return vertical_dataPF


# In[13]:

# def verify(tids):
#     tids = list(tids)
#     tids.sort()
#     if(len(tids)>0):
#         cur = tids[0]
#     pf = 0
#     for j in range(1, len(tids)):
#         if (tids[j] - cur <= per):
#             pf += 1
#         cur = tids[j]
#     return pf

# In[11]

def verify(tids):
    tids = list(tids)
    tids.sort()
    if (len(tids) > 0):
        cur = tids[0]
    pf = 0
    for j in range(1, len(tids)):
        if(tids[j] - cur <= per):
            pf += 1
        cur = tids[j]
    return pf

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
    for j in data:
        init_nbh.add(j)
        if j not in nbh_dict:
            nbh_dict[j]=set()
    
    print('Finished reading data..... \n Starting mining .....')
    # print(verify(data['234'][0]))
    k=eclat([], sorted(data.items(), key=lambda item: item[1][1], reverse=False),init_nbh )
    # print('found %d Frequent items' % len(FreqItems))
    with open(sys.argv[5], 'w') as f:
        for x in k:
            f.write('%s \n'%str(x))