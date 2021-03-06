# -*- coding: utf-8 -*-
"""Heart Disease.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MBSJ6HIlwaEEOHyVSEQM-VpAvqkPZNK9
"""

import numpy as np
import pandas as pd

"""numpy is used for linear algebra and pandas is used for data processing and reading files.

"""

df = pd.read_csv('dataset.csv')
df.head(5)

"""df.head(5) shows the rows and columns of the file here the 5 in paarenthesis gives us 5 rows."""

df.info()

"""prints a consise summery of the dataset of its datatypes,non-null values and memeory size."""

import seaborn as sns
import matplotlib.pyplot as plt

sns.countplot(x=df['Heart Disease'],hue='Sex',data=df)

sns.countplot(x=df['Heart Disease'],hue='Chest pain type',data=df)

sns.countplot(x=df['Sex'],hue='Chest pain type',data=df)

sns.barplot(x=df['Sex'],y=df['BP'],data=df)

sns.barplot(x=df['Sex'],y=df['Cholesterol'],data=df)

sns.barplot(x=df['Heart Disease'],y=df['Cholesterol'],data=df)

sns.barplot(x=df['Heart Disease'],y=df['BP'],data=df)

sns.lineplot(x=df['Age'],y=df['BP'],data=df)

sns.lineplot(x=df['Age'],y=df['Cholesterol'],data=df)

sns.lineplot(x=df['Age'],y=df['ST depression'],data=df)

sns.barplot(x=df['Sex'],y=df['ST depression'],data=df)

sns.barplot(x=df['Heart Disease'],y=df['Exercise angina'],data=df)

sns.barplot(x=df['Sex'],y=df['Exercise angina'],data=df)

sns.barplot(x=df['Heart Disease'],y=df['Number of vessels fluro'],data=df)

sns.barplot(x=df['Heart Disease'],y=df['Thallium'],data=df)

sns.barplot(x=df['Sex'],y=df['FBS over 120'],data=df)

sns.heatmap(df.corr())

from sklearn.preprocessing import LabelEncoder,StandardScaler
le=LabelEncoder()
df['Heart Disease']=le.fit_transform(df['Heart Disease'])

y=df['Heart Disease']
x=df.drop(['Heart Disease'],axis=1)

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=0,test_size=0.2)

from sklearn.neighbors import KNeighborsClassifier
list_1=[]
for i in range(1,21):
    knn=KNeighborsClassifier(n_neighbors=i)
    knn.fit(x_train,y_train)
    preds=knn.predict(x_test)
    scores=accuracy_score(y_test,preds)
    list_1.append(scores)

max(list_1)

from sklearn.linear_model import LogisticRegression
lr=LogisticRegression(max_iter=10000)
lr.fit(x_train,y_train)
pred_1=lr.predict(x_test)
score_1=accuracy_score(y_test,pred_1)
print(score_1)