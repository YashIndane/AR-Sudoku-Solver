from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
import pandas as pd
import cv2
import joblib

# Building the Random Forest Classifier

# importing file
data = pd.read_csv('Digits_Dataset.csv' , header = None)
#data = data.sample(frac = 1).reset_index(drop = True)
X = data.iloc[: , : 529].values
Y = data.iloc[: , 529 : 530].values


# splitting training and test data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.05, random_state = 0)


# Training the model
classifier = RandomForestClassifier(n_estimators = 117 , criterion = 'entropy')
classifier.fit(X_train, Y_train)
joblib.dump(classifier , 'RFC_160')


# predictions
y_pred = classifier.predict(X_test)
print(confusion_matrix(Y_test , y_pred))
print(classifier.score(X_test , Y_test))




