import pickle
import sqlite3
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import warnings

warnings.filterwarnings('ignore')


class Train():
    def __init__(self, model, data_path, table_name):
        self.data_path = data_path
        self.model = model
        self.X_train, self.X_valid, self.y_train, self.y_valid = self.load_data(
            table_name)

        self.train_model()

    def train_model(self):
        self.model.fit(self.X_train, self.y_train)

    def load_data(self, table_name):
        conn = sqlite3.connect(self.data_path)
        df = pd.read_sql_query("SELECT * FROM {}".format(table_name),
                               conn,
                               )
        print(df.head())
        X = df.iloc[:, 2:].values
        y = df.iloc[:, 1].values
        X_train, X_valid, y_train, y_valid = train_test_split(
            X, y, test_size=0.3, random_state=42)
        return X_train, X_valid, y_train, y_valid

    def predict(self):
        return self.model.predict(self.X_valid)

    def score(self):
        print('Train Score: {}'.format(
            round(self.model.score(self.X_train, self.y_train), 3)))
        print('Valid Score : {}'.format(
            round(self.model.score(self.X_valid, self.y_valid), 3)))


if __name__ == "__main__":
    model = LogisticRegression(random_state=42)
    result = Train(model, "sample.db", "train_feature_1")
    result.score()

    pkl_file = "LR_model.pkl"
    with open(pkl_file, 'wb') as f:
        pickle.dump(result.model, f)
