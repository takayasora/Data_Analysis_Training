import pandas as pd

df = pd.read_csv("Book\Sukkiri_ML\ProjectA\datafiles\cinema.csv")
df2 = df.fillna(df.mean())

no = df2[(df2['SNS2']>1000) & (df2["sales"]<8500)].index
df3 = df2.drop(no,axis=0)

x = df3[['SNS1','SNS2','actor','original']]
t = df3["sales"]

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,t,test_size=0.2,random_state=0)

from sklearn.linear_model import LinearRegression
model = LinearRegression()

print(model.fit(x_train,y_train))
print(model.score(x_test,y_test))

new = [[150,700,300,0]]
print(model.predict(new))

from sklearn.metrics import median_absolute_error
pred = model.predict(x_test)

print(median_absolute_error(y_pred=pred,y_true=y_test))

import pickle

with open("Book\Sukkiri_ML\ProjectA\cinema.pkl","wb") as f:
    pickle.dump(model,f)