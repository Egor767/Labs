import numpy as np
from math import sqrt

def myMSE(test, predict):
    sum = 0
    test = test.tolist()
    for i in range(len(test)):
        sum += (test[i] - predict[i])**2
    return sum/len(test)

def myMAE(test, predict):
    test = test.tolist()
    sum = 0
    for i in range(len(test)):
        sum += abs(test[i] - predict[i])
    return sum/len(test)

def myRMSE(test, predict):
    sum = 0
    test = test.tolist()
    for i in range(len(test)):
        sum += (test[i] - predict[i])**2
    return sqrt(sum/len(test))

def myMAPE(test, predict):
    sum = 0
    test = test.tolist()
    for i in range(len(test)):
        if test[i] == 0:
            sum += (2 * (abs(test[i] - predict[i]))) / (test[i] + predict[i])
        else:
            sum += abs((test[i] - predict[i]) / test[i])   
    return sum/len(test)

def myR2(test, predict):
    sum, sum2 = 0, 0
    avg = test.mean()
    test = test.tolist()
    for i in range(len(test)):
        sum += (test[i] - avg)**2
        sum2 += (test[i] - predict[i])**2
        
    return 1 - (sum2/sum)