import numpy as np
from sklearn.svm import LinearSVC
import _pickle as cPickle
import torch
import csv
from sklearn.metrics import *
import random
random.seed(3)

# Reading data                                                                
f = open('./pickles/dataset_mean_train.pkl', 'rb')
X_train, y_train = cPickle.load(f)
f = open('./pickles/dataset_mean_test.pkl', 'rb')
X_test, y_test = cPickle.load(f)
f = open('./pickles/dmfeatures_train.pkl', 'rb')
X_etrain = cPickle.load(f)
f = open('./pickles/dmfeatures_test.pkl', 'rb')
X_etest = cPickle.load(f)

# Converting into appropriate datatypes for training
X_train = X_train.numpy()
X_test = X_test.numpy()
y_test = torch.FloatTensor(y_test)

X_train = np.concatenate((X_train,X_etrain),axis=1)
X_test = np.concatenate((X_test,X_etest),axis=1)

# Model initialization and training
clf = LinearSVC(max_iter = 10000)
clf.fit(X_train,y_train)
y_pred = clf.predict(X_test)

y_pred = y_pred.numpy()
y_test = y_test.numpy()

print("Accuracy", accuracy_score(y_pred,y_test))
print("F1", f1_score(y_pred,y_test))
print("Precision",precision_score(y_pred,y_test))
print("Recall",recall_score(y_pred,y_test))
print("Confusion Matrix:")
print(confusion_matrix(y_pred,y_test))
