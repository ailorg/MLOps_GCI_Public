import pandas as pd
import sqlite3
import sys
import os

def execute_preprocessing():
    base = os.path.dirname(os.path.abspath(__file__))
    file = os.path.normpath(os.path.join(base, '../../sample.db'))
    conn = sqlite3.connect(file)

    for train_test in ["train", "test"]:
        save_table_name = train_test + "_feature_1"

        df = pd.read_sql_query(f'SELECT * FROM {train_test}', conn)

        missing_list = ['Age', 'Fare', 'Cabin', 'Embarked']
        df.drop(missing_list, axis=1, inplace=True)

        category_list = ['Name', 'Sex', 'Ticket']
        df.drop(category_list, axis=1, inplace=True)

        df = df.iloc[:, 1:]
        df.to_sql(save_table_name, conn, if_exists='replace', index=True)
        print(f"Done :{save_table_name} table")
