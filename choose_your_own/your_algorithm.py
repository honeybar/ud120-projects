#!/usr/bin/python

import matplotlib.pyplot as plt

from class_vis import prettyPicture, output_image
from prep_terrain_data import makeTerrainData
from email_preprocess import preprocess

features_train, labels_train, features_test, labels_test = makeTerrainData()
#features_train, labels_train, features_test, labels_test = preprocess()

### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]




### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

from sklearn.neighbors import KNeighborsClassifier

clf = KNeighborsClassifier(weights="distance", n_neighbors=10 )
clf.fit(features_train,labels_train)
pred = clf.predict(features_test)
from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)
print acc



#### initial visualization
##plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
