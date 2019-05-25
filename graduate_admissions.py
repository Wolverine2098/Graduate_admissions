# -*- coding: utf-8 -*-
"""
Created on Sat May 25 18:00:08 2019

@author: Logan
"""

import numpy as np
import pandas as pd
import csv
s=0
dataset=pd.read_csv('admin_predict.csv')
Y=dataset.iloc[:,8:9].values
X=dataset.iloc[:,1:8].values
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=1/4,random_state=0) 
from sklearn.svm import SVR   
classifier=SVR()
classifier.fit(X_train,Y_train.ravel())

while 1:
 s=0
 print("Graduate admission prediction tool")
 a=float(input("Enter your GRE score "))
 b=float(input("Enter your TOEFL score "))
 c=float(input("Enter your University Rating score "))
 d=float(input("Enter your SOP score "))
 e=float(input("Enter your LOR score "))
 f=float(input("Enter your CGPA score "))
 g=float(input("Enter your Research score "))
 dataset=pd.read_csv('admin_predict.csv')
 Y_pres=classifier.predict([[a,b,c,d,e,f,g]])
 print("Your chance of admission for graduation is ",Y_pres*100,"%")
 
 s=int(input("press 1 to continue and 0 to exit "))
 if s==0:
     break
 
