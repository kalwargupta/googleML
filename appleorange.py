#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 08:54:03 2019

@author: jeetu
"""

from sklearn import tree

features=[[140,0],[130,0],[150,1],[170,1]]
lable=["apple","apple","orange","orange"]
clf=tree.DecisionTreeClassifier()
clf=clf.fit(features,lable)

print(clf.predict([[120,1]]))