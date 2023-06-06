from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import cross_val_score
import pandas as pd
import numpy as np
import pickle
# from sklearn.preprocessing import OneHotEncoder

df = pd.read_csv('finaldataset.csv')
xf = df[['keyword', 'grammar', 'qst']]
# intigrate keyword, grammar, qst :)
''''
keywords and qst:
e = 1
vg = 2
g = 3
o = 4
p = 5
vp = 6

Grammar:
y = 1
n = 0

class labels 0.1 to 0.9 simplifies to 0 to 9 for calculation purpose
'''

# x = np.array(xf.values)
# yf = df[['class']]
# y = np.array(yf.values).ravel()
# clf = GaussianNB()
# clf.fit(x,y)
# scores = cross_val_score(clf, x, y, cv=10)
# print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

# with open('nav_test.pickle','wb') as f:
# 	pickle.dump(clf, f)

pickle_in = open('nav_test.pickle', 'rb')
clf = pickle.load(pickle_in)


def predict(k, g, q):
    predicted = clf.predict([[k, g, q]])
    accuracy = clf.predict_proba([[k, g, q]])
    print("class[1-9] : " + str(predicted))
    accuracy = round(np.max(accuracy) * 100, 2)
    # print(accuracy)
    # print(np.max(accuracy))
    return predicted

# predict(2,0,4)
# predict for 
# 1. keyword = verygood(2), grammar = no(0), qst = ok(4) 
# => 6
# 2. keyword = verygood(2), grammar = no(0), qst = vg (2)
# => 8


# print(yf.values)
# x= np.array([[-3,7],[1,5], [1,2], [-2,0], [2,3], [-4,0], [-1,1], [1,1], [-2,2], [2,7], [-4,1], [-2,7]])
# y = np.array([3, 3, 3, 3, 4, 3, 3, 4, 3, 4, 4, 4])
# # lx= np.array(
# 	[
# 		['e','y','e'],
# 		['e','n','e'],
# 		['vg','n','e'],
# 		['e','y','vg'],
# 		['e','n','g']
# 	]
# 	)
# ly = np.array(
# 	[
# 		0.9,
# 		0.9,
# 		0.8,
# 		0.8,
# 		0.7
# 	]
# 	)


# model = GaussianNB()

# # model.fit(lx,ly)
# model.fit(x,y)

# predict(6,1,4)
