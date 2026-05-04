from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import os
import pickle

x,y=load_iris(return_X_y=True)

model = RandomForestClassifier()
model.fit(x,y)

#os.makedirs("model",exist_ok=True)
with open("model.pkl","wb")as f:
    pickle.dump(model,f)
    
print("Model trained and saved....")