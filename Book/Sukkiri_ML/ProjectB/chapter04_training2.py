import pandas as pd

df = pd.read_csv("Book\Sukkiri_ML\ProjectA\datafiles\KvsT.csv")

xcol=["身長","体重","年代"]
x=df[xcol]
t=df["派閥"]

from sklearn import tree

model = tree.DecisionTreeClassifier(random_state=0)
print(model.fit(x,t))

print(model.score(x,t))