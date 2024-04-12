import pandas as pd
import numpy as np

df = pd.read_csv("https://raw.githubusercontent.com/futurexskill/projects/main/knn-classification/purchase_history.csv")

df.head()

df.count()

len(df)

gender_encoded = pd.get_dummies(df['Gender'])

gender_encoded

gender_encoded = pd.get_dummies(df['Gender'],drop_first=True)

gender_encoded

df = pd.concat([df,gender_encoded],axis=1)

df

x = df[['Male','Age','Salary','Price']].to_numpy()

x

y = df['Purchased'].to_numpy()

y

from sklearn.model_selection import train_test_split

x_train , x_test , y_train , y_test = train_test_split(x,y, test_size=0.2, random_state=42)

x_train

x_test

y_train

y_test

len(x_train)

len(x_test)

len(y_train)

len(y_test)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

x_train = scaler.fit_transform(x_train)
x_test = scaler.fit_transform(x_test)

x_train

x_test

from sklearn.neighbors import KNeighborsClassifier

k= 5
knn = KNeighborsClassifier(n_neighbors=k)

knn.fit(x_train,y_train)

y_pred = knn.predict(x_test)

y_pred

y_test

from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, y_pred)
accuracy

import pickle

with open('knn_model.pickle','wb') as f:
  pickle.dump(knn,f)

with open('scaler.pickle','wb') as f:
  pickle.dump(scaler,f)