import pandas as pd

#データの読み込み   
df=pd.read_csv("Book\Sukkiri_ML\ProjectA\datafiles\iris.csv")

#欠損値の埋め込み
colmean = df.mean(numeric_only=True)
print(colmean)
df2 = df.fillna(colmean)

#特徴量と正解データに分割
xcol = ["がく片長さ","がく片幅","花弁長さ","花弁幅"]
x = df2[xcol]
t = df2["種類"]

#モデルの学習と準備
from sklearn import tree
model = tree.DecisionTreeClassifier(max_depth=2,random_state=0)

#訓練データとテストデータを分割
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,t,test_size=0.3,random_state=0)

#正解率の計算
print(model.fit(x_train,y_train))
print(model.score(x_test,y_test))

#モデルを保存する
import pickle
with open("Book\Sukkiri_ML\ProjectA\irismodel.pkl","wb") as f:
    pickle.dump(model,f)