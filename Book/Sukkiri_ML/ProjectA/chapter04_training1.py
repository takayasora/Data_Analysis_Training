import pandas as pd

#データの読み込み
df=pd.read_csv("Book\Sukkiri_ML\ProjectA\datafiles\KvsT.csv")

#特徴量と正解データに分割
xcol = ["身長","体重","年代"]
x = df[xcol]
t = df["派閥"]

#モデルの学習と準備
from sklearn import tree
model = tree.DecisionTreeClassifier(random_state=0)
print(model.fit(x,t))

#正解率の計算
print(model.score(x,t))