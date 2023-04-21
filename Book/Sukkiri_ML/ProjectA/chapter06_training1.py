import pandas as pd
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