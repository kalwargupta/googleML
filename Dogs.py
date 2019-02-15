#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 09:22:02 2019

@author: jeetu
"""

import numpy as np
import matplotlib.pyplot as plt

#Dogs name

greyhounds=500
labra=500

#dogs height
grey_height=28 + 4 * np.random.randn(greyhounds)
labra_height=24 + 4 * np.random.randn(labra) 

plt.hist([grey_height,labra_height], stacked=True, color=['r','b'])
plt.show()