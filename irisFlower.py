#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 09:07:46 2019

@author: jeetu
"""
import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree
iris=load_iris()


'''
print (iris.feature_names)
print (iris.target_names)
print (iris.target )

print (iris.data[100])

for i in range(len(iris.target)):
    print ( "Example %d: lable %s: , features %s " %( i, iris.target_names, iris.data[i])  )
'''

test_idx=[0,50,100]

#Training data
train_traget= np.delete(iris.target, test_idx)
train_data=np.delete(iris.data,test_idx,axis=0)
print (train_traget)
'''
print (train_data)
count1 =0
count2 =0
count3 =0
for i in range(len(train_data)):
    if train_data[i]==0:
        count1 +=1
    elif train_data[i]==1:
        count2+=1
    else:
        count3+=1
print(count2)
'''

#testing data

test_target=iris.target[test_idx]
test_data=iris.data[test_idx]

#print (test_data)

clf=tree.DecisionTreeClassifier()
clf.fit(train_data,train_traget)

print (clf.predict(test_data))

#vizulaization code

from sklearn.externals.six import StringIO
import pydot
dot_data=StringIO()
tree.export_graphviz(clf,
                     out_file=dot_data,
                     feature_names=iris.feature_names,
                     class_names=iris.target_names,
                     filled=True, rounded=True,
                     impurity=False)


graph = pydot.graph_from_dot_data(dot_data.getvalue())
graph[0].write_pdf("iris.pdf") 
print (test_data[0],test_target[0])
