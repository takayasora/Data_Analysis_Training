# 必要なライブラリをインポート
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from supervised.automl import AutoML

train = pd.read_csv(r"SIGNATE\【練習問題】お弁当の需要予測\original\train.csv")
test = pd.read_csv(r"SIGNATE\【練習問題】お弁当の需要予測\original\test.csv")
sample = pd.read_csv(r"SIGNATE\【練習問題】お弁当の需要予測\original\sample.csv", header=None)

# 分析用の説明変数を選択しておく
anacols = ["datetime", "week", "soldout", "name", "kcal", "remarks", "event", "payday", "weather", "precipitation"]
# Xとyの作成
X_train = train[anacols] # 説明変数
y_train = train["temperature"] # 目的変数
X_test = test[anacols] # 説明変数
y_test = test["temperature"] # 目的変数

# mljarのautomlモデルを作成
automl = AutoML(results_path=r"SIGNATE\【練習問題】お弁当の需要予測\outputML\"")
automl.fit(X_train, y_train)

# 予測対象のサンプルデータにweek列を追加
sample.columns = ["datetime", "temperature"]
sample["week"] = pd.to_datetime(sample["datetime"]).dt.week

# サンプルデータに対して予測を行う
sample_predictions = automl.predict_all(sample)

# 予測結果を正しいフォーマットに整形
submission = sample_predictions[["datetime", "prediction"]]
submission.columns = ["datetime", "temperature"]
submission["datetime"] = pd.to_datetime(submission["datetime"]).dt.strftime("%Y-%m-%d")

# 予測結果を出力
submission.to_csv("submit_sample.csv", index=False)
