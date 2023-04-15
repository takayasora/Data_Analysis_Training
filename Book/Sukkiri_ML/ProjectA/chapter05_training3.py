import pandas as pd
from sklearn import tree
from sklearn.model_selection import train_test_split
import pickle

df = pd.read_csv("Book\Sukkiri_ML\ProjectA\datafiles\iris.csv")

x = df[["がく片長さ", "がく片幅", "花弁長さ", "花弁幅"]]
t = df["種類"]

model = tree.DecisionTreeClassifier(max_depth=2, random_state=0)
x_train, x_test, y_train, y_test = train_test_split(x, t, test_size=0.3, random_state=0)
