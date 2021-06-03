import pandas as pd
import sqlite3
import sys

file = "sample.db"
conn = sqlite3.connect(file)

try:
    train_test = sys.argv[1]
except IndexError:
    print(
        "Index Error: Expected Value 'train' or 'test' is missing."
        "You should type like 'python preprocessing.py train'")
    sys.exit()
train_test = sys.argv[1]
save_table_name = train_test + "_feature_1"

df = pd.read_sql_query(f'SELECT * FROM {train_test}', conn)

missing_list = ['Age', 'Fare', 'Cabin', 'Embarked']
df.drop(missing_list, axis=1, inplace=True)

category_list = ['Name', 'Sex', 'Ticket']
df.drop(category_list, axis=1, inplace=True)

df = df.iloc[:, 1:]
df.to_sql(save_table_name, conn, if_exists='replace', index=True)
print(f"Done :{save_table_name} table")
