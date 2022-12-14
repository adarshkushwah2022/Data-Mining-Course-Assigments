# -*- coding: utf-8 -*-
"""DMG ASSIGNMENT 3 Q2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pBn-pA5qyvwrh0iNuhKOgTD1AzTPpwCu

**Inference Code**
"""

# Commented out IPython magic to ensure Python compatibility.
# import statements
import pickle
import warnings
import numpy as np
# %matplotlib inline
import pandas as pd
from numpy import asarray
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore")
from sklearn.metrics import f1_score
from matplotlib import pyplot as plt
from sklearn.mixture import GaussianMixture
from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import train_test_split
from scipy.cluster.vq import whiten, kmeans, vq, kmeans2


# other functions


def predict(test_set) :
  #Loading the best model
  fileName='/content/drive/MyDrive/DMG ASSIGNMENT 3/bestModelDmgAssignment3Q2.sav'
  loaded_model = pickle.load(open(fileName, 'rb'))
  df=pd.read_csv(test_set)
  majorityLabels={0:2,1:2,2:2,3:2,4:1,5:2,6:2}
  
  #Pre-processing the Test dataset

  #ordinal encoding of string categorical features
  l=asarray(df['Elevation'])
  l1=np.reshape(l,(len(l),1))
  enc = OrdinalEncoder()
  enc.fit(l1)
  result = enc.fit_transform(l1)
  for x in range(len(result)):
    result[x]=int(result[x])
  df['Elevation']=result
  df['Elevation'] = df['Elevation'].astype(int)

  l=asarray(df['Aspect'])
  l1=np.reshape(l,(len(l),1))
  enc = OrdinalEncoder()
  enc.fit(l1)
  result = enc.fit_transform(l1)
  for x in range(len(result)):
    result[x]=int(result[x])
  df['Aspect']=result
  df['Aspect'] = df['Aspect'].astype(int)

  l=asarray(df['Slope'])
  l1=np.reshape(l,(len(l),1))
  enc = OrdinalEncoder()
  enc.fit(l1)
  result = enc.fit_transform(l1)
  for x in range(len(result)):
    result[x]=int(result[x])
  df['Slope']=result
  df['Slope'] = df['Slope'].astype(int)

  l=asarray(df['Hillshade_9am'])
  l1=np.reshape(l,(len(l),1))
  enc = OrdinalEncoder()
  enc.fit(l1)
  result = enc.fit_transform(l1)
  for x in range(len(result)):
    result[x]=int(result[x])
  df['Hillshade_9am']=result
  df['Hillshade_9am'] = df['Hillshade_9am'].astype(int)

  l=asarray(df['Hillshade_Noon'])
  l1=np.reshape(l,(len(l),1))
  enc = OrdinalEncoder()
  enc.fit(l1)
  result = enc.fit_transform(l1)
  for x in range(len(result)):
    result[x]=int(result[x])
  df['Hillshade_Noon']=result
  df['Hillshade_Noon'] = df['Hillshade_Noon'].astype(int)

  l=asarray(df['Horizontal_Distance_To_Fire_Points'])
  l1=np.reshape(l,(len(l),1))
  enc = OrdinalEncoder()
  enc.fit(l1)
  result = enc.fit_transform(l1)
  for x in range(len(result)):
    result[x]=int(result[x])
  df['Horizontal_Distance_To_Fire_Points']=result
  df['Horizontal_Distance_To_Fire_Points'] = df['Horizontal_Distance_To_Fire_Points'].astype(int)
 
  # normalize the values of all input features present in the df2 dataframe
  X = whiten(df)

  #Performing TSNE(T-distributed Stochastic Neighbor Embedding) on the Test dataset
  #TSNE will reduce the number of features to two
  from sklearn.manifold import TSNE
  c_tsne = TSNE(n_components=2).fit_transform(X)
  c_tsne=pd.DataFrame(c_tsne)

  #Predicting the clusters
  clustersTest  = loaded_model.predict(c_tsne)
  #Finding corresponding true label for the training instances using predicted cluster 
  predictedTrueLabel=[]
  for eachCluster in clustersTest:
    predictedTrueLabel.append(majorityLabels[eachCluster])
  
  prediction=predictedTrueLabel
  return prediction