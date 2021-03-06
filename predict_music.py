
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
# from sklearn import tree
# import joblib
music_data = pd.read_csv(r"C:\Users\junha\PythonProjects\predict_music_preferences\music.csv")
# print(music_data)


X = music_data.drop(columns=['genre'])
y = music_data['genre']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
print(predictions)

score = accuracy_score(y_test, predictions)
print(score)

# joblib.dump(model, 'music-recommender.joblib')

# tree.export_graphviz(model, out_file='music-recommender.dot',
# feature_names=['age', 'gender'],
# class_names=sorted(y.unique()), 
# label='all', rounded= True,
# filled=True)