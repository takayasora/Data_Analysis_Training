import pandas as pd
from sklearn import tree

df = pd.read_csv("Book\Sukkiri_ML\ProjectA\datafiles\KvsT.csv")

x = df[["身長","体重","年代"]]
t = df["派閥"]

model = tree.DecisionTreeClassifier(random_state=0)
print(model.fit(x,t))
print(model.score(x,t))