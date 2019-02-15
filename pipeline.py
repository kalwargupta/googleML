#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 10:25:56 2019

@author: jeetu
"""

from sklearn import datasets
iris=datasets.load_iris()

x=iris.data
y=iris.target

#from sklearn.cross_validation import train_test_split
#previous version  cross_validation
#this is the latest version model_slection
from sklearn.model_selection import train_test_split
x_Train,x_Test,y_Train,y_Test = train_test_split(x, y, test_size=.5)


from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
KNclf=KNeighborsClassifier()
DTclf=tree.DecisionTreeClassifier()

DTclf = DTclf.fit(x_Train,y_Train)
KNclf=KNclf.fit(x_Train,y_Train)

DTprediction=DTclf.predict(x_Test)
KNprediction=KNclf.predict(x_Test)

print (y_Test)
print (DTprediction)
print (KNprediction)

from sklearn.metrics import accuracy_score
DTaccuracy= accuracy_score(y_Test, DTprediction)
KNaccuracy=accuracy_score(y_Test, KNprediction)
print (DTaccuracy)
print (KNaccuracy)