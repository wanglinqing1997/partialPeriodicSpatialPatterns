#!/usr/bin/env python
# coding: utf-8

# In[8]:

import sys
import datetime
import time
import progressbar

FreqItems = dict()
per=float(sys.argv[1])
per_freq=float(sys.argv[2])
final_data=dict()
nbh_dict=dict()

def eclat(prefix, items,nbh_prefix):
    while items:
        i, itids = items.pop()
        # print(itids)
        # print("++++++")
        # print(items)
        isupp = len(itids)
        # FreqItems[frozenset(prefix + [i])] = isupp
        yield (prefix + [i],itids[1])
        nbh_sent = nbh_prefix & nbh_dict[i]
        # print(prefix + [i])
        suffix = []
        for j, ojtids in items:
            if j in nbh_sent:
                jtids = itids[0] & ojtids[0]
                pf_alpha = verify(jtids)
                if pf_alpha >= per_freq:
                    suffix.append((j,[jtids,pf_alpha]))
        # print(suffix)
        for pat in eclat(prefix+[i], sorted(suffix, key=lambda item: item[1][1], reverse=False),nbh_sent):
            yield pat

def Read_Data(filename):
    vertical_data = {}
    trans = 0
    with open(filename, 'r') as f:
        for row in f:
            k=row.split()
            for item in k[1:]:
                if item not in vertical_data:
                    vertical_data[item] = set()
                vertical_data[item].add(int(k[0]))
    vertical_dataPF={}
    for k in vertical_data:
        perf_k=verify(vertical_data[k])
        if perf_k>=per_freq:
            vertical_dataPF[k]=[vertical_data[k],perf_k]
    # print(vertical_dataPF['127'])
    # final_data={ k: v for k, (v,verify(v)) in data.items() if  verify(v)==0}
    return vertical_dataPF

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
    return pf

if __name__ == "__main__":
    start_time = datetime.datetime.now()
    dict_id = 0
    data = Read_Data(sys.argv[3]) #change the delimiter based on your input file
    with open(sys.argv[4],'r') as nbh:
        for line in nbh:
            #print(line)
            li = line.split()
            if li[0] in data:
                ds = set()
                for i in range(1, len(li)):
                    if li[i] in data:
                        ds.add(li[i])
                nbh_dict[li[0]] = ds
    init_nbh = set()
    for j in data:
        init_nbh.add(j)
        if j not in nbh_dict:
            nbh_dict[j] = set()
    print('Finished reading data... \nStarting mining ...')
    # print(verify(data['234'][0]))
    k=eclat([], sorted(data.items(), key=lambda item: item[1][1], reverse=False), init_nbh)
    # print('found %d Frequent items' % len(FreqItems))
    # 调用Eclat算法
    with open(sys.argv[5], 'w') as f:
        progress = progressbar.ProgressBar()
        # 进度条代码，不想用可以删掉。
        for x in progress(k):
            f.write('%s \n'%str(x))
    end_time = datetime.datetime.now()
    cost_time = end_time - start_time
    print('Mining time:{}'.format(cost_time))

