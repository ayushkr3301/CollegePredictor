# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 22:15:39 2019

@author: hp
"""

# Importing the libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import keras
import tensorflow
import theano



# Importing the dataset
df = pd.read_csv('Admission_Predict_Ver1.1.csv')
X = df.iloc[:, 1:8].values
y = df.iloc[:, 8].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


# Importing the Keras libraries and packages
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout


# Initialising the ANN
classifier = Sequential()

# Adding the input layer and the first hidden layer
classifier.add(Dense(units = 4, kernel_initializer = 'uniform', activation = 'sigmoid', input_dim = 7))
classifier.add(Dropout(p = 0.1))

# Adding the second hidden layer
classifier.add(Dense(units = 4, kernel_initializer = 'uniform', activation = 'sigmoid'))
classifier.add(Dropout(p = 0.1))


# Adding the output layer
classifier.add(Dense(units = 1, kernel_initializer = 'uniform', activation = 'sigmoid'))


# Compiling the ANN
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])



# Fitting the ANN to the Training set
classifier.fit(X_train, y_train, batch_size = 10, epochs = 100)



# Predicting the Test set results
y_pred = classifier.predict(X_test)
y_pred = (y_pred > 0.65)


y_test = (y_test > 0.65)


damn = sc.transform(np.array([[int(input('Marks obtained in GRE - ')), 
                               int(input('Marks obtained in TOEFL - ')),
                               float(input('Rating of university out of 5 - ')),
                               float(input('Study Oriented Projects(no.) - ')), 
                               float(input('Letters Of Reccomendation(no.) - ')), 
                               float(input('CGPA - ')), 
                               int(input('Research done -- 1ForYes-0ForNo - '))]]))
new_prediction = classifier.predict(damn)
print('Probablity of getting admission -->> ', new_prediction)



# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)



# Evaluating the ANN
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import cross_val_score
from keras.models import Sequential
from keras.layers import Dense
def build_classifier():
    classifier = Sequential()
    classifier.add(Dense(units = 4, kernel_initializer = 'uniform', activation = 'sigmoid', input_dim = 7))
    classifier.add(Dense(units = 4, kernel_initializer = 'uniform', activation = 'sigmoid'))
    classifier.add(Dense(units = 1, kernel_initializer = 'uniform', activation = 'sigmoid'))
    classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
    return classifier
classifier = KerasClassifier(build_fn = build_classifier, batch_size = 10, epochs = 100)
accuracies = cross_val_score(estimator = classifier, X = X_train, y = y_train, cv = 10, n_jobs = 1)
mean = accuracies.mean()
variance = accuracies.std()





