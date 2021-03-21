#!/usr/bin/python
from __future__ import division
import matplotlib.pyplot as plt
import math
import sys

def read (file_name):
    features = []
    labels = []
    f= open(file_name)
    for line in f:
        feature1, feature2, label = line.strip().split(" ")
        labels.append(int(label))
        features.append([1, float(feature1) , float(feature2)])
    return [labels, features]
    f.close()

file_name = sys.argv[1]
deneme = read(file_name)
weights=[0.1,0.1,0.1]

def dot_product(values,weights):
    dot_product = sum(x*w for x,w in zip(values,weights))
    return dot_product

while True:
    counter = 0
    #i = labels , j = features
    for i,j in zip(deneme[0],deneme[1]):
        s = dot_product(j,weights)
        if (s*i) < 0:
            counter    += 1
            weights[0] += i * j[0]
            weights[1] += i * j[1]
            weights[2] += i * j[2]
    if counter == 0:
        break

label_positive_1 = []
label_negative_1 = []
for i,j in zip(deneme[0],deneme[1]):
    if i == 1:
        label_positive_1.append(j)
    else:
        label_negative_1.append(j)
label_positive_1_f1 = []
label_positive_1_f2 = []
label_negative_1_f1 = []
label_negative_1_f2 = []
for line in label_negative_1:
    label_negative_1_f1.append(line[1])
    label_negative_1_f2.append(line[2])
for line in label_positive_1:
    label_positive_1_f1.append(line[1])
    label_positive_1_f2.append(line[2])

def function(x1,weights):
    x2 = (weights[0] + (weights[1] * x1)) / weights[2]
    return x2
X1_1 = function(min(label_negative_1_f1),weights)
X1_2 = function(max(label_negative_1_f1),weights)

print X1_1, X1_2

plt.scatter(label_negative_1_f1, label_negative_1_f2, color = "r")
plt.scatter(label_positive_1_f1, label_positive_1_f2, color = "b")
plt.plot (X1_1,X1_2)

plt.show()