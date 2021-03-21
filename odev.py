#!/usr/bin/python
import sys
import math

def read ( fname ):
    features = []
    labels = []
    f = open ( fname )
    for line in f:
        idx, distance, torsion = line.split(" ")
        if (int(idx)<2 or int(idx)>4): continue
        labels.append( int(idx) )
        features.append ( [ float(distance), float(torsion) ] )
            #print distance
    f.close()
    return [labels, features]

def seperated ( labels, features ):
    uniq_labels = set(labels)
    print uniq_labels
    out = {}
    for uniq in uniq_labels:
        out[uniq]={'X':[], 'Y':[]}
    for F, L in zip(features, labels):
        out[L]['X'].append(F[0])
        out[L]['Y'].append(F[1])
    return out

fname = sys.argv[1]
All_Labels, All_Features = read(fname)
All_Length = len(All_Labels)
Train_Length = int(All_Length*0.9)
Train_Labels = All_Labels[:Train_Length]
Train_Features = All_Features[:Train_Length]
Test_Labels = All_Labels[Train_Length:]
Test_Features = All_Features[Train_Length:]

my_seperated = seperated (Train_Labels, Train_Features)

mean_distance2 = sum(my_seperated[2]['X']) / len(my_seperated[2]['X'])
mean_distance3 = sum(my_seperated[3]['X']) / len(my_seperated[3]['X'])
mean_distance4 = sum(my_seperated[4]['X']) / len(my_seperated[4]['X'])
mean_torsion2  = sum(my_seperated[2]['Y']) / len(my_seperated[2]['Y'])
mean_torsion3  = sum(my_seperated[3]['Y']) / len(my_seperated[3]['Y'])
mean_torsion4  = sum(my_seperated[4]['Y']) / len(my_seperated[4]['Y'])

total_sum = 0
for i in my_seperated[2]['X']:
    total_sum = total_sum + (i - mean_distance2 ) ** 2
variance_distance2 = math.sqrt (total_sum / len(my_seperated[2]['X']))

total_sum = 0
for i in my_seperated[3]['X']:
    total_sum = total_sum + (i - mean_distance3 ) ** 2
variance_distance3 = math.sqrt (total_sum / len(my_seperated[3]['X']))

total_sum = 0
for i in my_seperated[4]['X']:
    total_sum = total_sum + (i - mean_distance4 ) ** 2
variance_distance4 = math.sqrt (total_sum / len(my_seperated[4]['X']))

total_sum = 0
for i in my_seperated[2]['Y']:
    total_sum = total_sum + (i - mean_torsion2 ) ** 2
variance_torsion2 = math.sqrt (total_sum / len(my_seperated[2]['Y']))

total_sum = 0
for i in my_seperated[3]['Y']:
    total_sum = total_sum + (i - mean_torsion3) ** 2
variance_torsion3 = math.sqrt (total_sum / len(my_seperated[3]['Y']))

total_sum = 0
for i in my_seperated[4]['Y']:
    total_sum = total_sum + (i - mean_torsion4 ) ** 2
variance_torsion4 = math.sqrt (total_sum / len(my_seperated[4]['Y']))

def gaussian_function (variance,mean,X):
    gaussian = (1/(variance * math.sqrt (2* math.pi))) * math.exp(( - (X - mean) ** 2 ) / (2 * (variance ** 2) ))
    return gaussian

def my_function (distance,torsion,x):
    probability = distance * torsion * x
    return probability

Train_Length = len(Train_Labels)
counter2 = 0
counter3 = 0
counter4 = 0
for i in Train_Labels:
    if i==2:
        counter2 = counter2 + 1
    elif i==3:
        counter3 = counter3 + 1
    else:
        counter4 = counter4 + 1
P2 = counter2 / float(Train_Length)
P3 = counter3 / float(Train_Length)
P4 = counter4 / float(Train_Length)

Predict_Labels = []

for x,y in Test_Features:
    gaussian_distance2 = gaussian_function(variance_distance2,mean_distance2,x)
    gaussian_torsion2  = gaussian_function(variance_torsion2 ,mean_torsion2 ,y)
    gaussian_distance3 = gaussian_function(variance_distance3,mean_distance3,x)
    gaussian_torsion3  = gaussian_function(variance_torsion3 ,mean_torsion3 ,y)
    gaussian_distance4 = gaussian_function(variance_distance4,mean_distance4,x)
    gaussian_torsion4  = gaussian_function(variance_torsion4 ,mean_torsion4 ,y)
    my_function2 = my_function(gaussian_distance2,gaussian_torsion2,P2)
    my_function3 = my_function(gaussian_distance3,gaussian_torsion3,P3)
    my_function4 = my_function(gaussian_distance4,gaussian_torsion4,P4)
    print my_function2, my_function3, my_function4
    if max(my_function2,my_function3,my_function4) == my_function2:
        Predict_Labels.append(2)
    elif max(my_function2,my_function3,my_function4) == my_function3:
        Predict_Labels.append(3)
    else:
        Predict_Labels.append(4)

def accuracy ( predict, test ):
    success = 0
    for a, b in zip(predict, test):
        if a == b: success += 1
    return float(success)/ len(predict)

my_accuracy = accuracy(Predict_Labels,Test_Labels)

print my_accuracy


















