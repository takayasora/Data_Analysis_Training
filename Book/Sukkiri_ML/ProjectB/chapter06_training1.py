import pandas as pd
<<<<<<< Updated upstream
df = pd.read_csv('Book\Sukkiri_ML\ProjectA\datafiles\cinema.csv')
df.isnull().any(axis=0)

df2 = df.fillna(df.mean())

no = df2[(df2['SNS2']>1000) & (df2["sales"]<8500)].index
df3 = df2.drop(no,axis=0)

col = ['SNS1','SNS2','actor','original']
x = df3[col] #特徴量の取り出し

t = df3['sales']

#スライス構文で特徴量と正解データを取り出す
x = df3.loc[:,'SNS1':'original']    #特徴量の取り出し
t = df3['sales']    #正解ラベルの取り出し

#訓練データとテストデータに分類する
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,t,test_size=0.2,random_state=0)
=======

#CSVファイルの読み込み
df = pd.read_csv("Book\Sukkiri_ML\ProjectA\datafiles\cinema.csv")

#欠損値の穴埋め
df2 = df.fillna(df.mean())
df2.isnull().any(axis=0)

#外れ値を削除する
no = df2[(df2['SNS2']>1000) & (df2["sales"]<8500)].index
df3 = df2.drop(no,axis=0)

#特徴量の列の候補
x = df3[['SNS1','SNS2','actor','original']]
t = df3['sales']

#訓練データとテストデータに分類する
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,t,test_size=0.2,random_state=0)

#重回帰モデルのLinearRegression関数をインポートする
from sklearn.linear_model import LinearRegression
model = LinearRegression()

#モデルの学習と評価
print(model.fit(x_train,y_train))
print(model.score(x_test,y_test))

#学習後のモデルで予測
new = [[150,700,300,0]]
print(model.predict(new))

#MAEを求める
#関数のインポート
from sklearn.metrics import median_absolute_error

pred = model.predict(x_test)

#平均絶対誤差の計算
print(median_absolute_error(y_pred=pred,y_true=y_test))

#モデルの保存
import pickle

with open("Book\Sukkiri_ML\ProjectA\cinema.pkl","wb") as f:
    pickle.dump(model,f)
>>>>>>> Stashed changes
