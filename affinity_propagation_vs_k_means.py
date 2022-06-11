# -*- coding: utf-8 -*-
"""Affinity Propagation VS K-Means.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13PwxjZM8Gsw53DCGh9G2n_kBy-bEw51Y
"""

from sklearn.cluster import KMeans
from sklearn import datasets
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import proj3d



import pandas as pd
import numpy as np
import seaborn as sns

#0 Iris 데이터 로드

iris = datasets.load_iris()

data = pd.DataFrame(iris.data) ; data

feature = pd.DataFrame(iris.feature_names) ; feature

data.columns = feature[0]

target = pd.DataFrame(iris.target) ; target
target.columns = ['target']
df = pd.concat([data,target], axis=1)

df. head()

df.info()



df = df.astype({'target' : 'object'})


df_copy = df.copy()
df. describe()

sns.pairplot(df_copy, hue = "target")
plt.show()

fig = plt.figure(figsize = (5,5))
x = df_copy

plt.plot(x.iloc[:,0]
         , x.iloc[:,3]
         , 'o'
         , markersize = 5
         , color = 'blue'
         , alpha = 0.5
         , label = 'class1')

plt.xlabel = ('x')
plt.ylabel = ('y')

plt.legend()
plt.show()

fig = plt.figure(figsize = (8,8))
axis = fig.add_subplot(111, projection = '3d')

x2 = df_copy
axis.scatter( x2.iloc[:,0], x2.iloc[:,1], x2.iloc[:,2], s = 12, cmap = 'orange', alpha = 1, label = 'class1')

plt.legend()
plt.show()

#1        K-Means 알고리즘
from importlib import reload


ks = range(1,10)
inertias = []

for i in ks:
  model = KMeans(n_clusters = i)
  model.fit(df_copy)
  inertias.append(model.inertia_)


plt.figure(figsize=(4,4))
plt.plot(ks, inertias, '-o')

plt.xticks(ks)

plt.show()

KMeans_clustmodel = KMeans(n_clusters = 7)

KMeans_clustmodel.fit(df_copy)

centers = KMeans_clustmodel.cluster_centers_
pred = KMeans_clustmodel.predict(df_copy)

print(pd.DataFrame(centers))
print(pred[:10])

clust_df = df_copy.copy()
clust_df['clust'] = pred
clust_df.head()

plt.figure(figsize = (20,6))

x3 = clust_df

plt.subplot(131)
sns.scatterplot(x=x3.iloc[:,0], y=x3.iloc[:,1], data = df_copy, hue = KMeans_clustmodel.labels_, palette = 'coolwarm')
plt.scatter(centers[:,0], centers[:,1], c = 'black', alpha = 1, s = 150)

plt.subplot(132)
sns.scatterplot(x=x3.iloc[:,0], y=x3.iloc[:,2], data = df_copy, hue = KMeans_clustmodel.labels_, palette = 'coolwarm')
plt.scatter(centers[:,0], centers[:,2], c = 'black', alpha = 1, s = 150)

plt.subplot(133)
sns.scatterplot(x=x3.iloc[:,0], y=x3.iloc[:,3], data = df_copy, hue = KMeans_clustmodel.labels_, palette = 'coolwarm')
plt.scatter(centers[:,0], centers[:,3], c = 'black', alpha = 1, s = 150)

fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(111,projection = '3d')

x4 = clust_df

ax.scatter(x3.iloc[:,0], x3.iloc[:,1], x3.iloc[:,2], c = x3.clust, s = 10, cmap = 'rainbow', alpha = 1)

ax.scatter(centers[:,0], centers[:,1], centers[:,2], c = 'black', s= 200, marker = '*')

#2 Affinity Propagation 

from sklearn.datasets import make_blobs
from sklearn.cluster import AffinityPropagation
from sklearn.metrics import *

x4 = iris.data
y = iris.target

Affinity_model = AffinityPropagation(random_state=None,preference = -50)
Af_prop = AffinityPropagation(max_iter = 300)
Af_prop.fit(x4)
center = Af_prop.cluster_centers_indices_

Af_prop.labels_

len_cluster = len(center)
print(center)

fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(111,projection = '3d')

x4 = clust_df

ax.scatter(x4.iloc[:,0], x4.iloc[:,1], x4.iloc[:,2], c = Af_prop.labels_, s = 10, cmap = 'rainbow', alpha = 1)
ax.scatter(centers[:,0], centers[:,1], centers[:,2], c = 'black', s= 200, marker = '*')

