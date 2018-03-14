#!/usr/bin/python
import csv
import numpy as np
from math import log
from decimal import *

datafile=open('baseball_train_set.csv', 'r')
datareader=csv.reader(datafile, delimiter=',')
bballtrain=[]
for row in datareader:
    bballtrain.append(row)

datafile2=open('hockey_train_set.csv', 'r')
datareader2=csv.reader(datafile2, delimiter=',')
hkytrain=[]
for row in datareader2:
    hkytrain.append(row)
    
print np.shape(bballtrain)
bbcounts=np.empty(5822, dtype=int)
for col in range(1, len(bballtrain[0])):
    for row in range(1, 50):
        bbcounts[col]+=int(bballtrain[row][col])
print np.shape(hkytrain)
hkcounts=np.empty(5822, dtype=int)
for col in range(1, len(hkytrain[0])):
    for row in range(1, 50):
        hkcounts[col]+=int(hkytrain[row][col])

def log_bball_prob(i):
    if bbcounts[i]==0:
        return 0
    elif sum(bbcounts)==0:
        return 0
    else:
        return log(Decimal(bbcounts[i])/Decimal(sum(bbcounts)))
def log_hky_prob(i):
    if hkcounts[i]==0:
        return 0
    elif sum(hkcounts)==0:
        return 0
    else:
        return log(Decimal(hkcounts[i])/Decimal(sum(hkcounts)))


datafile=open('baseball_test_set.csv', 'r')
datareader=csv.reader(datafile, delimiter=',')
bballtest=[]
for row in datareader:
    bballtest.append(row)

datafile=open('hockey_test_set.csv', 'r')
datareader=csv.reader(datafile, delimiter=',')
hkytest=[]
for row in datareader:
    hkytest.append(row)

def bball_prob(doc, row):
    btest_prob=0
    for col in range(1, len(bballtest[0])):
        btest_prob+=log_bball_prob(col)*int(doc[row][col])
    return btest_prob

def hky_prob(doc,row):
    htest_prob=0
    for col in range(1, len(hkytest[0])):
        htest_prob+=log_hky_prob(col)*int(doc[row][col])
    return htest_prob

def classify(doc,i):
    if bball_prob(doc,i)>=hky_prob(doc,i):
        return 1
    else:
        return 0
#1 represents baseball, 0 represents hockey

bball_class=np.empty(50, dtype=int)
for row in range(1,50):
    bball_class[row]=classify(bballtest,row)

print 'accuracy rate for baseball_test_set: ' + sum(bball_class)/50

hky_class=np.empty(50, dtype=int)
for row in range(1,50):
    hky_class[row]=classify(hkytest,row)

print 'accuracy rate for hockey_test_set: ' + (50-sum(hky_class))/50

