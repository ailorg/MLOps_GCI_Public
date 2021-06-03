import pickle
import pandas as pd
import sqlite3


class Inference():
    def __init__(self, model_path, data_path, table_name):
        self.model_path = model_path
        self.data_path = data_path
        self.data = self.load_data(table_name)
        self.__model = self.load_model

    @property
    def load_model(self):
        with open(self.model_path, 'rb') as file:
            trained_model = pickle.load(file)
        return trained_model

    def load_data(self, table_name):
        conn = sqlite3.connect(self.data_path)
        X = pd.read_sql_query("SELECT * FROM {}".format(table_name),
                              conn,
                              )
        return X

    def predict(self):
        return self.__model.predict(self.data.iloc[:, 1:].values)


if __name__ == "__main__":
    model = Inference("LR_model.pkl", "sample.db", "test_feature_1")
    y_pred = model.predict()
    print(f'model path: {model.model_path}')
    print(f'y_pred[-5:]: {y_pred[-5:]}')
