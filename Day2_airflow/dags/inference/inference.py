import pickle
import pandas as pd
import sqlite3
import os


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


def execute_inference():
    base = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.normpath(os.path.join(base, '../../LR_model.pkl'))
    data_path = os.path.normpath(os.path.join(base, '../../sample.db'))
    model = Inference(model_path, data_path, "test_feature_1")
    y_pred = model.predict()
    print(y_pred[:5])
